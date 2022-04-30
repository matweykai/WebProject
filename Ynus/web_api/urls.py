from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('votes', views.VotesView.as_view(), name="votes"),
    path('votes/companies', views.VotedCompaniesView.as_view(), name="voted_companies"),
]
