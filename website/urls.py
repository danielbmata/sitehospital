from django.urls import path
from . import views

urlpatterns = [
        path('', views.inicio, name='inicio'),
        path('trabalhe_conosco/', views.trabalhe_conosco, name='trabalhe_conosco'),
        path('fale_conosco/', views.fale_conosco, name='fale_conosco'),
        path('enviar_cv/', views.enviar_cv, name='enviar_cv'),
        path('sobre_nos/', views.sobre_nos, name='sobre_nos'),


    ]

