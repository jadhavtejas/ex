from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='conatct'),
    path('visit_list/', views.Visit_list, name='Visit_list_api'),
    path('visit_details/<pk>', views.Visit_details, name='Visit_details_api'),
    path('visitdata/', views.VisitData, name='VisitData'),

    
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('main/', views.main, name='index'),
    
]
