from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView,UpdateView,TemplateView
from Employeeprofile.models import Employeeprofile
from Userprofile.models import UserProfile
from .models import HRprofile
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from HRprofile.forms import HrCreateForm,HrLoginForm,HrUpdateForm
from django.urls import reverse
from django.views import View


# Create your views here.

class HrIndexView(View):
    template_name = 'HRprofile/hr_index.html'

    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(UserProfile.objects.filter(userid = userid_))
        try:
            if UserProfile.objects.filter(userid = userid_):
                return HttpResponseRedirect(reverse('index'))
        except:
            return render(request,self.template_name)
        return render(request,self.template_name)

class HrLogout(View):
    def get(self,request,*args,**kwars):
        logout(request)
        return HttpResponseRedirect(reverse('hr_index'))   

class HrprofileCreateView(CreateView):
    form_class = HrCreateForm
    template_name = "HRprofile/hr_create.html"

    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(UserProfile.objects.filter(userid = userid_))
        if UserProfile.objects.filter(userid = userid_).exists():
            return HttpResponseRedirect(reverse('index'))
        else:
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
                return HttpResponseRedirect(reverse('hr_index'))
            else:
                return HttpResponse('<h1>Username or email already exist</h1>')
        return render(request, self.template_name, {'form': form})

class HrLoginView(CreateView):
    form_class = HrLoginForm
    template_name = 'HRprofile/hr_login.html'

    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        print(UserProfile.objects.filter(userid = userid_))
        if UserProfile.objects.filter(userid = userid_).exists():
            return HttpResponseRedirect(reverse('hr_index'))
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.cleaned_data
            username = instance['username']   
            password = instance['password']
            user = authenticate(username = username,password = password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('hr_index'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")

class HrListView(ListView):
    template_name = 'HRprofile/hr_list.html'

    def get_queryset(self,*args,**kwargs):
        if UserProfile.objects.filter(userid=self.request.user).exists():
            return HttpResponseRedirect(reverse('index'))
        elif Employeeprofile.objects.filter(userid=self.request.user).exists():
            return HttpResponseRedirect(reverse('employee_index'))
        else:
            return UserProfile.objects.filter(status_l1='hired').filter(status_l1 = 'hired').filter(status_hr = 'pending')
            
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(HrListView,self).dispatch(request,*args,**kwargs)

class HrSelectListView(ListView):
    template_name = 'HRprofile/hr_selectlist.html'
    def get_queryset(self,*args,**kwargs):
        return UserProfile.objects.filter(status_l1='hired').filter(status_l1 = 'hired').filter(status_hr = 'hired')
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(HrSelectListView,self).dispatch(request,*args,**kwargs)

class HrRejectListView(ListView):
    template_name = 'HRprofile/hr_rejectlist.html'
    def get_queryset(self,*args,**kwargs):
        return UserProfile.objects.filter(status_l1='hired').filter(status_l1 = 'hired').filter(status_hr = 'reject')
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(HrRejectListView,self).dispatch(request,*args,**kwargs)

class HrUpdateView(View):
    template_name = "HRprofile/hr_update.html"
    form_class = HrUpdateForm
    
    def get(self, request, *args, **kwargs):
        userid_ = self.request.user
        if UserProfile.objects.filter(userid = userid_).exists():
            return HttpResponseRedirect(reverse('index'))
        elif Employeeprofile.objects.filter(userid=self.request.user).exists():
            return HttpResponseRedirect(reverse('employee_index'))
        else:
            userid_ = self.kwargs.get('userid')
            qs = UserProfile.objects.filter(userid = userid_)
            first_name = HRprofile.objects.filter(userid=self.request.user).values('first_name')[0]['first_name']
            last_name = HRprofile.objects.filter(userid=self.request.user).values('last_name')[0]['last_name']
            full_name = first_name +' '+last_name
            form = self.form_class(initial = {'interviewer_name_hr':full_name})
            return render(request, self.template_name, {'form': form,'query':qs})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        userid_ = self.kwargs.get('userid')
        print(form.is_valid())
        if form.is_valid():
            post_values = request.POST.copy()
            UserProfile.objects.filter(userid=userid_).update(interviewer_name_hr = post_values['interviewer_name_hr'],status_hr = post_values['status_hr'],
            rating_hr = post_values['rating_hr'],level_hr= post_values['level_hr'],feedback_hr= post_values['feedback_hr'],expected_salary = post_values['expected_salary'])
            return HttpResponseRedirect(reverse('hr_index')) 
        else:
            userid_ = self.kwargs.get('userid')
            qs = UserProfile.objects.filter(userid = userid_)
            return render(request, self.template_name, {'form': form,'query':qs})
