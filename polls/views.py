# THIS IS THE OLD CODE
# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# These imports are necessary for the latestFivePollQuestions method and for use templates
from .models import Question
from .models import Choice
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from django.urls import reverse


def index(request):  # Method for create a view an return it
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):  # Method for looking a question
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Short version of detail method
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,'polls/detail.html',{'question': question})


# Without Try Exception
# response = "You're looking at question %s."
# return HttpResponse(response % question_id)
# With Try Exception


def results(request, question_id):  # Method for looking the results of a question
    # Without Template
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    # With Template
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):  # Voting on question
    # Dummy Version
    # return HttpResponse("You're voting on question %s." % question_id)
    # Real version
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice'])  # 'choice' refere to data by key name,
        # in this case, request.POST['choice'] returns the ID of the selected
        # choice, as a string. request.POST values are always strings.
    except(KeyError, Choice.DoesNotExist):  # Key Error: The user don't choose
        # a question, so the pk cause a KeyError because the choice wasn’t provided in POST data
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hit the back button
        # This is the URL to which the user will be redirected
        # You should always return an HttpResponseRedirect after successfully dealing with POST data
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def about(request):
    return HttpResponse("In this app, you can vote on questions, looking the results of question and other amazing things")

# Without Template
# def latestFivePollQuestions(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

# With Template


def latestFivePollQuestions(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # The context is a dictionary mapping template variable names to Python objects.
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Short version of latestFivePollQuestions
#    def latestFivePollQuestions(request):
#       latest_question_list = Question.objects.order_by('-pub_date')[:5]
#       context = {'latest_question_list': latest_question_list}
#       return render(request, 'polls/index.html', context)


def countVotes(request, choice_id):
    try:
        choice = Choice.objects.get(pk=choice_id)
    except Choice.DoesNotExist:
        raise Http404("Choice does not exist")
    context = {'choice': choice}
    return render(request, 'polls/count.html', context)
