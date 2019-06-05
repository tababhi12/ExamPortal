from django.contrib import admin
from .models import HRprofile

# Register your models here.

class HRprofilerAdmin(admin.ModelAdmin):
    list_display = ['userid','first_name','last_name','empid','email','phone']

admin.site.register(HRprofile,HRprofilerAdmin)