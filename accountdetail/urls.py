from django.contrib import admin
from django.urls import path
from accountdetail import views

urlpatterns = [
    path('',views.index,name='index'),
]