from django.urls import path
from . import views

urlpatterns = [
    #path('', views.inicio, name='inicio'),
    path('', views.crear_ubicacion, name='crear_ubicacion'),
    path('mapa/', views.mapa, name='mapa'),
    path("api/ubicaciones/", views.obtener_ubicaciones, name="APIubicaciones"),
    path("api/add-ubi/", views.inserta_ubicacion, name="APInueva"),
]