from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UserProfileForm,UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from Userprofile.models import UserProfile
from django.db.models import Q
from django.views import View

class UserLogout(View):
    def get(self,request,*args,**kwars):
        logout(request)
        return HttpResponseRedirect(reverse('index'))



# Create your views here.
class UserProfileView(CreateView):
    form_class = UserProfileForm
    template_name = 'Userprofile/register.html'
    # def get(self, request, *args, **kwargs):
    #         form = self.form_class()
    #         return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            instance = form.cleaned_data
            print(instance)
            username = instance['userid']   
            password = instance['password']
            email = instance['email']
            print(User.objects.filter(username = username).exists())
            print(User.objects.filter(email = email).exists())
            if not (User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists()):
                User.objects.create_user(username,email,password)
                user = authenticate(username = username,password = password)
                login(request,user)
                form.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('<h1>Username or email already exist</h1>')
        return render(request, self.template_name, {'form': form})

class UserLoginView(CreateView):
    form_class = UserLoginForm
    template_name = 'Userprofile/login.html'

    def get(self, request, *args, **kwargs):
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
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")


class UserListView(ListView):
    #model = UserProfile
    def get_queryset(self):
        #qs =  super(UserListView,self).get_queryset(*args,**kwargs)
        return UserProfile.objects.filter(userid=self.request.user)
    

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super(UserListView,self).dispatch(request,*args,**kwargs)
            

class UserDetailView(LoginRequiredMixin,DetailView):
 
    def get_object(self):
        userid_ = self.kwargs.get('userid')
        return get_object_or_404(UserProfile,userid = userid_)

    
