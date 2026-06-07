from django.urls import path
from . import views

urlpatterns = [
    #path('', views.inicio, name='inicio'),
    path('', views.crear_ubicacion, name='crear_ubicacion'),
    path('mapa/', views.mapa, name='mapa')
]