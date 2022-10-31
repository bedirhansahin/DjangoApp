from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from . models import Question, Choice
from django.views import generic
from django.urls import reverse
from django.utils import timezone


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list':latest_question_list,
        
#     }
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         context = {
#             'question':question
#         }
#         return render(request, 'polls/detail.html', context)
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question':question,
#     }

#     return render(request, 'polls/results.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


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
