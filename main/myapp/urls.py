from django.urls import path
from . import views

#create views here

urlpatterns = [
    path('', views.index),
]