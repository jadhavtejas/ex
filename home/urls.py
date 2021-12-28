from django.contrib import admin
from django.urls import path
from home import views
from home import serializer

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='conatct'),
    path('visit_details', views.Visit_details, name='Visite_details_api'),
]
