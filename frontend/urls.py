from django.urls import re_path
from . import views


app_name = 'frontend'
urlpatterns = [
    re_path('^beta\/?.*', views.index, name='index'),
]
