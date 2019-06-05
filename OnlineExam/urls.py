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
from QuestionAnswer.views import QuestionAnswerCreateView,QuestionAnswerListView,QuestionAnswerUpdateView,QuestionAnswerExamView
from Userprofile.views import UserProfileView,UserLoginView,UserListView,UserDetailView,UserLogout
from HRprofile.views import HrIndexView,HrLogout,HrprofileCreateView,HrListView,HrSelectListView,HrRejectListView,HrLoginView,HrUpdateView
from Employeeprofile.views import EmployeeListView,EmployeeprofileCreateView,EmployeeLogout,EmployeeLoginView,EmployeeUpdateView,EmployeeSelectListView,EmployeeRejectListView,EmployeeIndexView

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'Userprofile/index.html'),name = 'index'),
    path('admin/', admin.site.urls),
    path('register',UserProfileView.as_view(),name = 'register'),
    path('login',UserLoginView.as_view(),name = 'login'),
    path('exam',QuestionAnswerExamView.as_view(),name = 'exam'),
    re_path('logout',UserLogout.as_view(),name = 'logout'),
    path('userresult',UserListView.as_view(),name = 'result'),
    path('result/<userid>/',UserDetailView.as_view(),name='user_view'),
    path('employee/',EmployeeIndexView.as_view(),name = 'employee_index'),
    path('hr/',HrIndexView.as_view(),name = 'hr_index'),

    path('employee/create',EmployeeprofileCreateView.as_view(),name = 'employee_register'),
    path('hr/create',HrprofileCreateView.as_view(),name = 'hr_register'),
    
    path('employee/logout/',EmployeeLogout.as_view(),name = 'employee_logout'),
    path('hr/logout/',HrLogout.as_view(),name = 'hr_logout'),

    path('employee/login',EmployeeLoginView.as_view(),name = 'employee_login'),
    path('hr/login',HrLoginView.as_view(),name = 'hr_login'),
    
    path('employee/empresult',EmployeeListView.as_view(),name = 'employee_result'),
    path('hr/hrresult',HrListView.as_view(),name = 'hr_result'),

    path('employee/update/<userid>/',EmployeeUpdateView.as_view(),name = 'employee_update'),
    path('hr/update/<userid>/',HrUpdateView.as_view(),name = 'hr_update'),

    path('employee/select',EmployeeSelectListView.as_view(),name = 'employee_select'),
    path('hr/select',HrSelectListView.as_view(),name = 'hr_select'),

    path('employee/reject',EmployeeRejectListView.as_view(),name = 'employee_reject'),
    path('hr/reject',HrRejectListView.as_view(),name = 'hr_reject'),

    path('employee/createexam',QuestionAnswerCreateView.as_view(),name = 'employee_createexam'),
    path('employee/question',QuestionAnswerListView.as_view(),name = 'question'),
    # path('^employee/question/(?P<pk>\d+)/$',QuestionAnswerDetailView.as_view(),name = 'question_detail'),
    path('employee/question/(?P<pk>\d+)/update/$',QuestionAnswerUpdateView.as_view(),name = 'question_update'),

    
    
]
