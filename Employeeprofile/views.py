from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView,UpdateView,TemplateView
from .models import Employeeprofile
from .forms import EmployeeCreateForm,EmployeeLoginForm,EmployeeUpdateForm,EmployeeUpdateFormL2
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View
from Userprofile.models import UserProfile

# Create your views here.
class EmployeeIndexView(View):
    template_name = 'Employeeprofile/index.html'

    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(userid_)
        print(UserProfile.objects.filter(userid = userid_))
        try:
            if UserProfile.objects.filter(userid = userid_):
                return HttpResponseRedirect(reverse('index'))
        except:
            return render(request,self.template_name)
        return render(request,self.template_name)

class EmployeeLogout(View):
    def get(self,request,*args,**kwars):
        logout(request)
        return HttpResponseRedirect(reverse('employee_index'))   

class EmployeeprofileCreateView(CreateView):
    form_class = EmployeeCreateForm
    template_name = "Employeeprofile/employee_create.html"

    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(userid_)
        print(UserProfile.objects.filter(userid = userid_))
        try:
            if UserProfile.objects.filter(userid = userid_):
                return HttpResponseRedirect(reverse('index'))
        except:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.cleaned_data
            username = instance['userid']
            password = instance['password']
            email = instance['email']
            if not (User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists()):
                User.objects.create_user(username,email,password)
                user = authenticate(username = username,password = password)
                login(request,user)
                form.save()
                return HttpResponseRedirect(reverse('employee_index'))
            else:
                return HttpResponse('<h1>Username or email already exist</h1>')
        return render(request, self.template_name, {'form': form})



class EmployeeLoginView(CreateView):
    form_class = EmployeeLoginForm
    template_name = 'Employeeprofile/employee_login.html'

    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(userid_)
        print(UserProfile.objects.filter(userid = userid_))
        try:
            if UserProfile.objects.filter(userid = userid_):
                return HttpResponseRedirect(reverse('index'))
        except:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            instance = form.cleaned_data
            username = instance['username']   
            password = instance['password']
            user = authenticate(username = username,password = password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('employee_index'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")


class EmployeeListView(ListView):
    template_name = 'Employeeprofile/employeeprofile_list.html'

    def get_queryset(self,*args,**kwargs):
        print(Employeeprofile.objects.filter(userid=self.request.user).exists())
        print(UserProfile.objects.filter(userid=self.request.user).exists())
        skill_ = Employeeprofile.objects.filter(userid=self.request.user).values('skill')[0]['skill']
        level = Employeeprofile.objects.filter(userid=self.request.user).values('level')[0]['level']
        print(skill_,level)
        if UserProfile.objects.filter(userid=self.request.user).exists():
            return HttpResponseRedirect(reverse('index'))
        elif Employeeprofile.objects.filter(userid=self.request.user).exists():
            if level == 'l1':
                return UserProfile.objects.filter(skill=skill_).filter(status_l1 = 'pending')
            else:
                return UserProfile.objects.filter(skill=skill_).filter(status_l1 = 'hired').filter(status_l2 = 'pending')
            
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(EmployeeListView,self).dispatch(request,*args,**kwargs)

class EmployeeSelectListView(ListView):
    template_name = 'Employeeprofile/employeeprofile_selectlist.html'
    def get_queryset(self,*args,**kwargs):
        first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
        last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
        name = first_name +' '+last_name
        skill_ = Employeeprofile.objects.filter(userid=self.request.user).values('skill')[0]['skill']
        level = Employeeprofile.objects.filter(userid=self.request.user).values('level')[0]['level']
        if level == 'l1':
            return UserProfile.objects.filter(skill=skill_).filter(interviewer_name_l1 = name).filter(status_l1 = 'hired')
        else:
            return UserProfile.objects.filter(skill=skill_).filter(interviewer_name_l2 = name).filter(status_l2 = 'hired')
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(EmployeeSelectListView,self).dispatch(request,*args,**kwargs)

class EmployeeRejectListView(ListView):
    template_name = 'Employeeprofile/employeeprofile_rejectlist.html'
    def get_queryset(self,*args,**kwargs):
        first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
        last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
        name = first_name +' '+last_name
        skill_ = Employeeprofile.objects.filter(userid=self.request.user).values('skill')[0]['skill']
        level = Employeeprofile.objects.filter(userid=self.request.user).values('level')[0]['level']
        if level == 'l1':
            return UserProfile.objects.filter(skill=skill_).filter(interviewer_name_l1 = name).filter(status_l1 = 'reject')
        else:
            return UserProfile.objects.filter(skill=skill_).filter(interviewer_name_l2 = name).filter(status_l2 = 'reject')
    
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(EmployeeRejectListView,self).dispatch(request,*args,**kwargs)


class EmployeeUpdateView(View):
    template_name = "Employeeprofile/employeeprofile_update.html"
    
    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(userid_)
        print(UserProfile.objects.filter(userid = userid_).exists())
        if UserProfile.objects.filter(userid = userid_).exists():
            return HttpResponseRedirect(reverse('index'))
        else:
            userid_ = self.kwargs.get('userid')
            level = UserProfile.objects.filter(userid = userid_).values('level_l1')[0]['level_l1']
            first_name = UserProfile.objects.filter(userid = userid_).values('first_name')[0]['first_name']
            last_name = UserProfile.objects.filter(userid = userid_).values('last_name')[0]['last_name']
            gender = UserProfile.objects.filter(userid = userid_).values('gender')[0]['gender']
            phone = UserProfile.objects.filter(userid = userid_).values('phone')[0]['phone']
            email = UserProfile.objects.filter(userid = userid_).values('email')[0]['email']
            experience = UserProfile.objects.filter(userid = userid_).values('experience')[0]['experience']
            notice_period = UserProfile.objects.filter(userid = userid_).values('notice_period')[0]['notice_period']
            print(level)
            first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
            print(first_name)
            last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
            name = first_name +' '+last_name
            print(last_name)
            print(name)
            interviewer_name_l1 = UserProfile.objects.filter(userid=userid_).values('interviewer_name_l1')[0]['interviewer_name_l1']
            print(interviewer_name_l1)
            if interviewer_name_l1:
                first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
                last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
                name = first_name +' '+last_name
                interviewer_name_l1 = UserProfile.objects.filter(userid = userid_).values('interviewer_name_l1')[0]['interviewer_name_l1']
                status_l1 = UserProfile.objects.filter(userid = userid_).values('status_l1')[0]['status_l1']
                rating_l1 = UserProfile.objects.filter(userid = userid_).values('rating_l1')[0]['rating_l1']
                feedback_l1 = UserProfile.objects.filter(userid = userid_).values('feedback_l1')[0]['feedback_l1']
                data = {'interviewer_name_l2':name,'userid':userid_,'first_name':first_name,'last_name':last_name,
                'gender':gender,'phone':phone,'email':email,'experience':experience,'notice_period':notice_period,
                'interviewer_name_l1':interviewer_name_l1,'status_l1':status_l1,'rating_l1':rating_l1,
                'feedback_l1':feedback_l1}
                form = EmployeeUpdateFormL2(initial = data)
                return render(request, self.template_name, {'form': form})

            else:
                print(self.request.user)
                first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
                print(first_name)
                last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
                name = first_name +' '+last_name
                data = {'interviewer_name_l1':name,'userid':userid_,'first_name':first_name,'last_name':last_name,
                'gender':gender,'phone':phone,'email':email,'experience':experience,'notice_period':notice_period}
                form = EmployeeUpdateForm(initial = data)
                return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print(self.kwargs.get('userid'))
        post_values = request.POST.copy()
        print(post_values)
        userid_ = self.kwargs.get('userid')
        level = UserProfile.objects.filter(userid = userid_).values('status_l1')[0]['status_l1']
        if not level == 'pending':
            form = EmployeeUpdateFormL2(post_values)
            print(form.is_valid())
            if form.is_valid():
                survey = get_object_or_404(UserProfile, userid=userid_)
                first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
                last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
                name = first_name +' '+last_name
                try :
                    if post_values['level_l2']:
                        level_value = True
                except:
                    level_value = False
                    pass
                UserProfile.objects.filter(userid=userid_).update(interviewer_name_l2 = name,status_l2 = post_values['status_l2'],
                rating_l2 = post_values['rating_l2'],level_l2= level_value,feedback_l2= post_values['feedback_l2'])
                return HttpResponseRedirect(reverse('employee_index'))   
        else:
            form = EmployeeUpdateForm(post_values)
            print(form.is_valid())
            if form.is_valid():
                survey = get_object_or_404(UserProfile, userid=userid_)
                # survey.interviewer_name_l1 = 'Abhishek Sahu'
                first_name = Employeeprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
                last_name = Employeeprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
                name = first_name +' '+last_name
                try :
                    if post_values['level_l1']:
                        level_value = True
                except:
                    level_value = False
                    pass
                UserProfile.objects.filter(userid=userid_).update(interviewer_name_l1 = name,status_l1 = post_values['status_l1'],
                rating_l1 = post_values['rating_l1'],level_l1= level_value,feedback_l1= post_values['feedback_l1'])
                return HttpResponseRedirect(reverse('employee_index'))  
            
        return render(request, self.template_name, {'form': form})

    

