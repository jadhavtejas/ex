from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='conatct'),
    path('visit_details', views.Visit_details, name='Visit_details_api'),
]
