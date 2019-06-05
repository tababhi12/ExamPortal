from django.db import models
from .validators import validate_phone,validate_userid,validate_email,validate_security_token

# Create your models here.

class HRprofile(models.Model):

    LEVEL_CHOICES = (('hr','HR'),)
    GENDER_CHOICES=(('m', 'Male'), ('f', 'Female'))

    userid                  = models.CharField(max_length = 120,null = False,unique = True,validators = [validate_userid],blank = False,verbose_name = 'Username')
    first_name              = models.CharField(max_length=120,null = False,blank = False,verbose_name = 'First Name')
    last_name               = models.CharField(max_length=120,null = False,blank = False,verbose_name = 'Last Name')
    gender                  = models.CharField(max_length = 120,choices = GENDER_CHOICES,verbose_name = 'Gender')
    empid                   = models.IntegerField(null = False,unique = True,blank = False,verbose_name = 'Employee ID')
    email                   = models.EmailField(null = True,unique = True,blank = True,validators = [validate_email],verbose_name = 'Email')
    phone                   = models.BigIntegerField(null = True,unique = True,blank = True,validators = [validate_phone],verbose_name = 'Phone Number')
    level                   = models.CharField(max_length = 120,null = False,blank = False,choices = LEVEL_CHOICES,default = 'hr')  
    hired                   = models.IntegerField(default = 0,null = True,blank = True,verbose_name = 'Total hired')
    rejected                = models.IntegerField(default = 0,null = True,blank = True,verbose_name = 'Total rejected')
    security_token          = models.CharField(max_length = 200,null = False,blank = False,verbose_name = 'Secure_token',validators = [validate_security_token])
    created_at              = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name = 'Created')
    updated_at              = models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name = 'Last Updated')


    class Meta:
        ordering = ['-created_at','-updated_at']
        verbose_name = 'HR'
        verbose_name_plural = 'HRs'