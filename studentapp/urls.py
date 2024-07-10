from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('register/',userregistration),
    path('login/',userlogin),
    path('index/',index),
    path('logout/',user_logout),
    path('create/',create),
    path('edit/<int:id>/', edit),
    path('update/<int:id>/', update),
    path('delete/<int:id>/', delete)


]