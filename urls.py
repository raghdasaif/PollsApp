from django.urls import path

#view is like a controller

from . import views

app_name = 'polls'
urlpatterns = [
    #ex: /polls/
    path('', views.index, name='index'),

    #ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    #ex: /polls/5/results/
    path('<int:question_id>/result/', views.result, name='result'),

    #ex: /polls/5/detail/
    #path('/<int:question_id>/detail/', views.detail, name='detail'),

    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]