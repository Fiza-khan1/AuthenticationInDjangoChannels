from django.contrib import admin
from django.urls import path
from .views import loginView,index
urlpatterns = [
    path('',index,name='index'),
    path("api/login/", loginView),
]