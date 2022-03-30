from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('/about_univ', views.univ_info, name="about_univ"),
]
