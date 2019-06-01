from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['userid','first_name','last_name','phone','email','experience','notice_period','skill','source','created_at','updated_at']

admin.site.register(UserProfile,UserProfileAdmin)
