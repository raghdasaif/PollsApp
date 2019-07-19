from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.all()
   # latest_question_list=Question.objects.order_by('-pub_date')[:1]   #top5 but did top1 bcz didnt include entries
    template = loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request,question_id):

    try:
     question = get_object_or_404(Question, pk=question_id)
     context1={
        'question': question,
    }
     template = loader.get_template('polls/detail.html')
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return HttpResponse(template.render(context1, request))

def result(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context2={
            'question':question,
            'error_message': "You didn't select a choice.",
        }
        template = loader.get_template('polls/detail.html')
        return HttpResponse(template.render(context2, request))
    else:
        selected_choice.votes+= 1
        selected_choice.save()
        # url generate through a view
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
