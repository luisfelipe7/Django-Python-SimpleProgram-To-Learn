from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/about
    path('about/', views.about, name='about'),
    # ex: /polls/latestFive
    path('latestFive/', views.latestFivePollQuestions, name='latestFive'),
    # ex: /polls/count
    path('<int:choice_id>/count/', views.countVotes, name='count'),

]
