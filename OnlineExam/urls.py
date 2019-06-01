"""OnlineExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from Userprofile import views
from django.views.generic.base import TemplateView
from Userprofile.views import UserProfileView,UserLoginView,UserListView,UserDetailView,UserLogout
from Employeeprofile.views import EmployeeListView,EmployeeprofileCreateView,EmployeeLogout,EmployeeLoginView,EmployeeUpdateView,EmployeeSelectListView,EmployeeRejectListView,EmployeeIndexView

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'Userprofile/index.html'),name = 'index'),
    path('admin/', admin.site.urls),
    path('register',UserProfileView.as_view(),name = 'register'),
    path('login',UserLoginView.as_view(),name = 'login'),
    re_path('logout',UserLogout.as_view(),name = 'logout'),
    path('result',UserListView.as_view(),name = 'result'),
    path('result/<userid>/',UserDetailView.as_view(),name='user_view'),
    path('employee/',EmployeeIndexView.as_view(),name = 'employee_index'),
    path('employee/create',EmployeeprofileCreateView.as_view(),name = 'employee_register'),
    path('employee/logout/',EmployeeLogout.as_view(),name = 'employee_logout'),
    path('employee/login',EmployeeLoginView.as_view(),name = 'employee_login'),
    path('employee/result',EmployeeListView.as_view(),name = 'employee_result'),
    path('employee/update/<userid>/',EmployeeUpdateView.as_view(),name = 'employee_update'),
    path('employee/select',EmployeeSelectListView.as_view(),name = 'employee_select'),
    path('employee/reject',EmployeeRejectListView.as_view(),name = 'employee_reject'),

    
    
]
