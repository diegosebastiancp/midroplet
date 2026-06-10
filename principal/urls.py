from django.urls import path
from . import views

urlpatterns = [
    #path('', views.inicio, name='inicio'),
    path('', views.mapa, name='mapa'),
    path("api/ubicaciones/", views.obtener_ubicaciones, name="APIubicaciones"),
    path("api/add-ubi/", views.inserta_ubicacion, name="APInueva"),
]