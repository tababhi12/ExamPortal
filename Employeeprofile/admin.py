from django.contrib import admin
from .models import Employeeprofile

class EmployeeprofileAdmin(admin.ModelAdmin):
    list_display = ['userid','first_name','last_name','empid','email','phone','level','skill']

# Register your models here.

admin.site.register(Employeeprofile,EmployeeprofileAdmin)
