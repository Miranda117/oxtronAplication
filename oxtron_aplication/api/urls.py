from django.urls import path
from . import views

urlpatterns = [


    path('api/welcome', views.welcome, name='welcome'),
    path('api/calculateScopeOne', views.calculateScopeOne, name='calculateScopeOne'),
    path('api/calculateTransportation', views.calculateTransportation, name='calculateTransportation'),
    path('api/calculateRefrigerantsPurchased', views.calculateRefrigerantsPurchased, name='calculateRefrigerantsPurchased')

]
