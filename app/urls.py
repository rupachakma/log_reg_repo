from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
]
