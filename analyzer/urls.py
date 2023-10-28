from django.urls import path
from .  import views

urlpatterns = [
    path('index/', views.index),
    path('analisar/', views.analisar, name='analisar'),
]