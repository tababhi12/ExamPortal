from django import forms
from .models import QuestionAnswer,UserQuestionAnswer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class QuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        exclude = ['question_id']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'skill',
            'question',
            'choice_a',
            'choice_b',
            'choice_c',
            'choice_d',
            'answer',
            Submit('submit', 'Create')
        )

class QuestionAnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        exclude = ['question_id']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'skill',
            'question',
            'choice_a',
            'choice_b',
            'choice_c',
            'choice_d',
            'answer',
            Submit('submit', 'Update')
        )

class QuestionAnswerUserForm(forms.ModelForm):
    class Meta:
        model = UserQuestionAnswer
        fields = ['answer_selected']
   