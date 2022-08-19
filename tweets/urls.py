from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path('', views.tweet_list_view, name='tweet-list'),
    path('create/', views.tweet_create_view, name='create-tweet'),
    path('action/', views.tweet_action_view, name='tweet-action'),
    path('<int:tweet_id>/', views.tweet_detail_view, name='tweet-details'),
    path('<int:tweet_id>/delete/', views.tweet_delete_view, name='tweet-delete'),

]