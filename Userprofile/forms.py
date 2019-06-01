from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(required = True,label = 'Password',max_length = 32,widget = forms.PasswordInput())
    class Meta:
        model = UserProfile
        fields = ['userid','password','first_name','last_name','gender','phone','email','experience','notice_period','skill','source']

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
                Column('experience', css_class='form-group col-md-6 mb-0'),
                Column('notice_period', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('skill', css_class='form-group col-md-6 mb-0'),
                Column('source', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Register')
        )





class UserLoginForm(forms.Form):
    username = forms.CharField(required = True,label = 'Username',max_length = 32)
    password = forms.CharField(required = True,label = 'Password',max_length = 32,widget = forms.PasswordInput())
    