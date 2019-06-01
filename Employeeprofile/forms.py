from django import forms
from .models import Employeeprofile
from Userprofile.models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class EmployeeCreateForm(forms.ModelForm):
    password = forms.CharField(required = True,label = 'Password',max_length = 200,widget = forms.PasswordInput())
    class Meta:
        model = Employeeprofile
        fields = ['userid','password','first_name','last_name','gender','empid','email','phone','level','skill','security_token']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('userid', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('empid', css_class='form-group col-md-6 mb-0'),
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'gender',
            Row(
                Column('phone', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('level', css_class='form-group col-md-6 mb-0'),
                Column('skill', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'security_token',
            Submit('submit', 'Register')
        )

    
class EmployeeLoginForm(forms.Form):
    username = forms.CharField(required = True,label = 'Username',max_length = 32)
    password = forms.CharField(required = True,label = 'Password',max_length = 32,widget = forms.PasswordInput())


class UpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['interviewer_name_l1','status_l1','rating_l1','feedback_l1','level_l1']


class EmployeeUpdateForm(UpdateForm):

    # STATUS_CHOICES = (('pending','Pending'),('hired','Hired'),('reject','Reject'))
    # RATING_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))

    userid = forms.CharField(required = False,max_length = 120,disabled =True)
    first_name = forms.CharField(required = False,max_length = 120,disabled =True)
    last_name = forms.CharField(required = False,max_length = 120,disabled =True)
    gender = forms.CharField(required = False,max_length = 120,disabled =True)
    phone = forms.CharField(required = False,max_length = 120,disabled =True)
    email = forms.CharField(required = False,max_length = 120,disabled =True)
    experience = forms.CharField(required = False,max_length = 120,disabled =True)
    notice_period = forms.CharField(required = False,max_length = 120,disabled =True)
    interviewer_name_l1 = forms.CharField(required = False,max_length = 120,disabled =True)
    # status_l1 = forms.ChoiceField(required = True,choices = STATUS_CHOICES)
    # rating_l1 = forms.ChoiceField(required = True,choices = RATING_CHOICES)
    # feedback_l1 = forms.CharField(widget = forms.Textarea,required = True,max_length = 240,label = 'L1 Feedback')
    # level_l1 = forms.BooleanField(required = True,label = 'L1 Level Done')

    class Meta:
        model = UserProfile
        fields = ['userid','first_name','last_name','gender','phone','email','experience','notice_period',
        'interviewer_name_l1','status_l1','rating_l1','feedback_l1','level_l1']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'userid',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gender', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            Row(
                Column('experience', css_class='form-group col-md-6 mb-0'),
                Column('notice_period', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'interviewer_name_l1',
            Row(
                Column('status_l1', css_class='form-group col-md-6 mb-0'),
                Column('rating_l1', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'feedback_l1',
            'level_l1',
            Submit('submit', 'Update')
        )

class UpdateFormL2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['interviewer_name_l2','status_l2','rating_l2','feedback_l2','level_l2']

class EmployeeUpdateFormL2(UpdateForm):
    
    STATUS_CHOICES = (('pending','Pending'),('hired','Hired'),('reject','Reject'))
    RATING_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))

    userid = forms.CharField(required = False,max_length = 120,disabled =True)
    first_name = forms.CharField(required = False,max_length = 120,disabled =True)
    last_name = forms.CharField(required = False,max_length = 120,disabled =True)
    gender = forms.CharField(required = False,max_length = 120,disabled =True)
    phone = forms.CharField(required = False,max_length = 120,disabled =True)
    email = forms.CharField(required = False,max_length = 120,disabled =True)
    experience = forms.CharField(required = False,max_length = 120,disabled =True)
    notice_period = forms.CharField(required = False,max_length = 120,disabled =True)
    interviewer_name_l1 = forms.CharField(required = False,max_length = 120,disabled =True)
    status_l1 = forms.ChoiceField(required = False,choices = STATUS_CHOICES,disabled =True)
    rating_l1 = forms.ChoiceField(required = False,choices = RATING_CHOICES,disabled =True)
    feedback_l1 = forms.CharField(widget = forms.Textarea,required = False,max_length = 240,label = 'L1 Feedback',disabled =True)

    class Meta:
        model = UserProfile
        fields = ['userid','first_name','last_name','gender','phone','email','experience','notice_period',
        'interviewer_name_l1','status_l1','rating_l1','feedback_l1',
        'interviewer_name_l2','status_l2','rating_l2','feedback_l2','level_l2',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'userid',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gender', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            Row(
                Column('experience', css_class='form-group col-md-6 mb-0'),
                Column('notice_period', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'interviewer_name_l1',
            Row(
                Column('status_l1', css_class='form-group col-md-6 mb-0'),
                Column('rating_l1', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'feedback_l1',
            'interviewer_name_l2',
            Row(
                Column('status_l2', css_class='form-group col-md-6 mb-0'),
                Column('rating_l2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'feedback_l2',
            'level_l2',
            Submit('submit', 'Update')
        )
 