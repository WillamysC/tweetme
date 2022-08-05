from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-tweet', views.tweet_create_view, name='create-tweet'),
    path('tweets', views.tweet_list_view, name='tweets-list'),
    path('tweets/<int:tweet_id>', views.tweet_detail_view, name='tweet-details'),
]