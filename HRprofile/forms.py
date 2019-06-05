from django import forms
from .models import HRprofile
from Userprofile.models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class HrCreateForm(forms.ModelForm):
    password = forms.CharField(required = True,label = 'Password',max_length = 200,widget = forms.PasswordInput())
    class Meta:
        model = HRprofile
        fields = ['userid','password','first_name','last_name','gender','empid','email','phone','level','security_token']

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
                Column('level', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'security_token',
            Submit('submit', 'Register')
        )

class HrLoginForm(forms.Form):
    username = forms.CharField(required = True,label = 'Username',max_length = 32)
    password = forms.CharField(required = True,label = 'Password',max_length = 32,widget = forms.PasswordInput())


class HrUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['interviewer_name_hr','status_hr','rating_hr','feedback_hr','expected_salary','level_hr']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'interviewer_name_hr',
            Row(
                Column('status_hr', css_class='form-group col-md-6 mb-0'),
                Column('rating_hr', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'feedback_hr',
            'level_hr',
            'expected_salary',
            Submit('submit', 'Update')
        )