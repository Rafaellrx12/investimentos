from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("cadastro/", views.cadastro, name='cadastro'),
    path("logar/", views.logar, name='logar'),
     path('logout/', views.logout_view, name='logout'),
    
]
