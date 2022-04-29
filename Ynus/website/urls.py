from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('/about_univ', views.univ_info, name="about_univ"),
    path('/about_project', views.project_info, name="project_info"),
    path('/directions_view', views.directions_view, name="directions_view"),
    path('direction/<int:pk>/', views.DirectionView.as_view(), name="direction_page"),
    path('register', views.SignUpView.as_view(), name='register'),
    path('auth', views.SignInView.as_view(), name='signin'),
    path('logout', views.logout_user, name='logout'),
]
