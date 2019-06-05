from django.db import models
from django.shortcuts import reverse

class QuestionAnswer(models.Model):

    SKILL_CHOICES = (('python','Python'),('java','Java'))
    ANSWER_CHOICE = (('a','Choice A'),('b','Choice B'),('c','Choice C'),('d','Choice D'))


    question_id =   models.AutoField(primary_key=True, verbose_name="ID")
    skill       =   models.SlugField(default = 'python',choices = SKILL_CHOICES,verbose_name = 'Skill')
    question =      models.TextField(max_length = 1000,verbose_name = 'Question',blank = False,null = False)
    choice_a =      models.CharField(max_length = 220,verbose_name = 'Choice 1',blank = False,null = False)
    choice_b =      models.CharField(max_length = 220,verbose_name = 'Choice 2',blank = False,null = False)
    choice_c =      models.CharField(max_length = 220,verbose_name = 'Choice 3',blank = False,null = False)
    choice_d =      models.CharField(max_length = 220,verbose_name = 'Choice 4',blank = False,null = False)
    answer =        models.CharField(default = 'a',max_length = 220,verbose_name = 'Answer',blank = False,null = False,choices = ANSWER_CHOICE)


    def get_absolute_url(self):
        return reverse("question_update", kwargs={"pk": self.question_id})

class UserQuestionAnswer(models.Model):
    ANSWER_CHOICE = (('a','Choice A'),('b','Choice B'),('c','Choice C'),('d','Choice D'))

    userid      =   models.CharField(max_length = 120,null = True,blank = True,unique = True,verbose_name = 'Username')
    question_id =   models.SmallIntegerField(null = True,blank = True,verbose_name = 'Question Id')
    answer_selected = models.CharField(default = 'a',max_length = 120,null = True,blank = True,unique = True,verbose_name = 'Answer',choices = ANSWER_CHOICE)
