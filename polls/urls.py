from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    # 一、form（表单形式）
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),

    # 二、generic views（通用视图）
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
