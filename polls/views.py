from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from . models import Question, Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
        
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        context = {
            'question':question
        }
        return render(request, 'polls/detail.html', context)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question,
    }

    return render(request, 'polls/results.html', context)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question,
        'error_message': "You didn't select a choice."
     }
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
