from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_list, name='post_list'),
]