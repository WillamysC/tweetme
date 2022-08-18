from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-tweet', views.tweet_create_view, name='create-tweet'),
    path('tweets', views.tweet_list_view, name='tweet-list'),
    path('tweets/<int:tweet_id>', views.tweet_detail_view, name='tweet-details'),
    path('api/tweets/<int:tweet_id>/delete', views.tweet_delete_view, name='tweet-delete'),

]