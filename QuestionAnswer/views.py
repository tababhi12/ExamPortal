from django.shortcuts import render,reverse,get_object_or_404
from django import views
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionAnswerForm,QuestionAnswerUpdateForm,QuestionAnswerUserForm
from Userprofile.models import UserProfile
from QuestionAnswer.models import QuestionAnswer
import re
import random
import numpy as np
from Employeeprofile.models import Employeeprofile
from Userprofile.models import UserProfile

# Create your views here.

class MultipleObjectMixin(object):
    	def get_object(self, queryset=None, *args, **kwargs):
            id = self.kwargs.get("pk")
            if id:
                try:
                    obj = self.model.objects.get(question_id=id)
                except self.model.MultipleObjectsReturned:
                    obj = self.get_queryset().first()
                except:
                    raise Http404
                return obj
            raise Http404

class QuestionAnswerCreateView(LoginRequiredMixin,CreateView):
    form_class = QuestionAnswerForm
    template_name = 'QuestionAnswer\questionanswer_create.html'

    def get(self,request,*args,**kwargs):
        userid_ = self.request.user
        if UserProfile.objects.filter(userid = userid_).exists():
            return HttpResponseRedirect(reverse('index'))
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employee_index'))

class QuestionAnswerListView(LoginRequiredMixin,ListView):

    def get_queryset(self,*args,**kwargs):
        if UserProfile.objects.filter(userid=self.request.user).exists():
            return HttpResponseRedirect(reverse('index'))
        skill_ = Employeeprofile.objects.filter(userid=self.request.user).values('skill')[0]['skill']
        return QuestionAnswer.objects.filter(skill = skill_)
    
class QuestionAnswerUpdateView(LoginRequiredMixin,UpdateView):
    model = QuestionAnswer
    form_class = QuestionAnswerUpdateForm
    template_name = 'QuestionAnswer\questionanswer_update.html'

    def get_success_url(self):
        return reverse("question")
             
class QuestionAnswerExamView(LoginRequiredMixin,views.View):
    template_name = 'QuestionAnswer\questionanswer_exam.html'
    form_class = QuestionAnswerUserForm 
    print('level 1')
    list_of_form = []
    registered = False
    n = 0
    answer_given = []
    correct_answer = []
    def get(self,request,*args,**kwargs):
        exam_done = UserProfile.objects.filter(userid=self.request.user).values('exam_done')[0]['exam_done']
        if not exam_done:
            return render(request,self.template_name,{'registered':self.registered})
        else:
            return HttpResponseRedirect(reverse('index'))
        

    def post(self,request,*args,**kwargs):
        print(self.registered)
        print(self.request.POST.get('active',None))
        qs = QuestionAnswer.objects.all()
        list_of_question = random.sample(range(1,len(qs)+1), 3)
        print(list_of_question)
        query = QuestionAnswer.objects.filter(question_id__in = list_of_question)
        print(query)
        self.correct_answer = [x.answer for x in qs]
        if self.request.POST.get('active',None) != 'Yes':
            form = self.form_class()
            self.registered = True
            return render(request,self.template_name,{'form':form,'queryset':query,'registered':self.registered})
        else:
            print(self.correct_answer)
            print(request.POST)
            self.answer_given = re.findall('\w',re.findall('(?<=answer_selected)(.*?)(?=\])',str(request.POST))[0])
            print(self.answer_given)
            score_ = len(['yes' for x,y in list(zip(self.correct_answer,self.answer_given)) if x == y])
            UserProfile.objects.filter(userid=self.request.user).update(score = score_)
            UserProfile.objects.filter(userid=self.request.user).update(exam_done = True)
            return HttpResponseRedirect(reverse('index'))
        # qs = QuestionAnswer.objects.all()
        # for query in qs:
        #     form = self.form_class()
        #     if self.n < 3:
        #         self.registered = True
        #         print(self.registered)
        #         return render(request,self.template_name,{'form':form,'question':query.question,
        #                                             'choice_a':query.choice_a,
        #                                             'choice_b':query.choice_b,
        #                                             'choice_c':query.choice_c,
        #                                             'choice_d':query.choice_d,
        #                                             'registered':self.registered})

# class QuestionAnswerDetailView(ModelFormMixin, MultipleObjectMixin,DetailView):
#     model = QuestionAnswer
#     form_class = QuestionAnswerForm

#     def get_context_data(self, *args, **kwargs):
#         context = super(QuestionAnswerDetailView, self).get_context_data(*args, **kwargs)
#         context["form"] = self.get_form()
#         return context

#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             self.object = self.get_object()
#             form = self.get_form()
#             if form.is_valid():
#                 return self.form_valid(form)
#             else:
#                 return self.form_invalid(form)

#     def get_success_url(self):
#         return reverse("question")

