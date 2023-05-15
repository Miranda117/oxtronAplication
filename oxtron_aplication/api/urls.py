from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.welcome, name='welcome'),
    path('api/', views.calculateStationaryCombustion, name='calculateStationaryCombustion'),
    path('api/', views.calculateMobileCombustion, name='calculateMobileCombustion'),
    path('api/', views.calculateRefrigerants, name='calculateRefrigerants'),
    path('api/', views.calculateTransportation, name='calculateTransportation'),
    path('api/', views.calculateRefrigerantsPurchased, name='calculateRefrigerantsPurchased')
]
