from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.gameState, name='play'),
    path('sign-in/', views.get_name, name='Sign In')
]