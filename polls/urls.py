from django.urls import path
from . import views

app_name = 'polls'

# Without Generic Views
# urlpatterns = [
# ex: /polls/
#    path('', views.index, name='index'),
# ex: /polls/5/
#    path('<int:question_id>/', views.detail, name='detail'),
# ex: /polls/5/results/
#   path('<int:question_id>/results/', views.results, name='results'),
# ex: /polls/5/vote/
#   path('<int:question_id>/vote/', views.vote, name='vote'),
# ex: /polls/about
#    path('about/', views.about, name='about'),
# ex: /polls/latestFive
#    path('latestFive/', views.latestFivePollQuestions, name='latestFive'),
# ex: /polls/count
#   path('<int:choice_id>/count/', views.countVotes, name='count'),
# ]

# With Generic Views (https://docs.djangoproject.com/en/2.1/topics/class-based-views/)
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:choice_id>/count/', views.countVotes, name='count'),
]

# What’s different in automated tests is that the testing work is done for you by the system.
# You create a set of tests once, and then as you make changes to your app, you can check that
# your code still works as you originally intended, without having to perform time consuming manual testing.
