from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('post-tweet',post_tweet.as_view(),name='post-tweet')
]
