from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('menu/', views.menu_detail, name='menu_detail'),

    
]
