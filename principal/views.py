from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UbicacionForm
from .models import ubicacion

def inicio(request):


    return HttpResponse("Prueba 1")

def crear_ubicacion(request):

    if request.method == 'POST':
        form = UbicacionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('crear_ubicacion')

    else:
        form = UbicacionForm()

    return render(request, 'ubicacion_form.html', {
        'form': form
    })

def mapa(request):

    ubicaciones = ubicacion.objects.all()

    return render(request, 'mapa.html', {
        'ubicaciones': ubicaciones
    })