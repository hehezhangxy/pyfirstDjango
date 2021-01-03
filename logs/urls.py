from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path(r'topics/(?P<topic_id>\d)', views.topic, name='topic')
]