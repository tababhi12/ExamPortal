from django.db import models
from .validators import validate_phone,validate_userid,validate_status_l1
from django.urls import reverse


# Create your models here.


#choices
SOURCE_CHOICES = (('referral','Referral'),('jop_portal','Job Portal'))
STATUS_CHOICES = (('pending','Pending'),('hired','Hired'),('reject','Reject'))
SKILL_CHOICES = (('python','Python'),('java','Java'))
RATING_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
GENDER_CHOICES=(('male', 'Male'), ('female', 'Female'))

class UserProfile(models.Model):

    #User Specific
    userid                  = models.CharField(max_length = 120,null = False,blank = False,unique = True,validators = [validate_userid],verbose_name = 'Username')
    first_name              = models.CharField(max_length=120,null = False,blank = False,verbose_name = 'First Name')
    last_name               = models.CharField(max_length=120,null = False,blank = False,verbose_name = 'Last Name')
    gender                  = models.CharField(max_length = 120,choices = GENDER_CHOICES,verbose_name = 'Gender')
    phone                   = models.BigIntegerField(null = False,blank = False,unique =True,validators = [validate_phone],verbose_name = 'Phone Number')
    email                   = models.EmailField(null = False,blank = False,unique =True,verbose_name = 'Email')          
    experience              = models.IntegerField(default = 2,blank = False,null =False,verbose_name = 'Experience')
    notice_period           = models.IntegerField(default = 0,blank = False,null =False,verbose_name = 'Notice Period')
    skill                   = models.SlugField(default = 'python',choices = SKILL_CHOICES,verbose_name = 'Skill')
    source                  = models.CharField(max_length = 10,choices = SOURCE_CHOICES,verbose_name = 'Source')


    #l1 level specific
    interviewer_name_l1     = models.CharField(max_length = 120,null = True,blank = True,verbose_name = 'L1 Interviewee Name')
    status_l1               = models.CharField(default = 'pending',max_length = 10,choices = STATUS_CHOICES,verbose_name = 'L1 Status',validators = [validate_status_l1])
    rating_l1               = models.IntegerField(null = True,blank = True,choices = RATING_CHOICES,verbose_name = 'l1 Rating')
    feedback_l1             = models.TextField(null = True,blank = True,verbose_name = 'L1 Feedback')
    level_l1                = models.BooleanField(default = True,verbose_name = 'L1 Level Done')

    #l2 level specific
    interviewer_name_l2     = models.CharField(max_length = 120,null = True,blank = True,verbose_name = 'L2 Interviewee Name')
    status_l2               = models.CharField(default = 'pending',max_length = 10,choices = STATUS_CHOICES,verbose_name = 'L2 Status',validators = [validate_status_l1])
    rating_l2               = models.IntegerField(null = True,blank = True,choices = RATING_CHOICES,verbose_name = 'L2 Rating')
    feedback_l2             = models.TextField(null = True,blank = True,verbose_name = 'L2 Feedback')
    level_l2                = models.BooleanField(default = True,verbose_name = 'L2 Level Done')



    created_at              = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name = 'Created')
    updated_at              = models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name = 'Last Updated')
    level                   = models.IntegerField(null = True,blank = True,verbose_name = 'Level Done')
    

    class Meta:
        ordering = ['-created_at','-updated_at']
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    
