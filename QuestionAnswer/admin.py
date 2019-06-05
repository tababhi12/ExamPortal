from django.contrib import admin
from .models import QuestionAnswer

# Register your models here.

class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['question_id','question','answer']

admin.site.register(QuestionAnswer,QuestionAnswerAdmin)