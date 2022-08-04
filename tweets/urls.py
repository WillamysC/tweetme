from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tweets', views.tweet_list_view, name='tweets-list'),
    path('tweets/<int:tweet_id>', views.tweet_detail_view, name='tweet-details'),
]