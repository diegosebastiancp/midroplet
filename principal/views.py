from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UbicacionForm
from .models import ubicacion
import json

def inicio(request):
    return HttpResponse("Prueba 1")

def mapa(request):

    if request.method == 'POST':
        form = UbicacionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('mapa')

    else:
        form = UbicacionForm()

    ubicaciones = ubicacion.objects.all()

    return render(request, 'mapa.html', {
        'ubicaciones': ubicaciones,
        'form': form
    })

# APIs ===========================================================
def obtener_ubicaciones(request):
    ubicaciones = ubicacion.objects.all().values(
        "id_ubi",
        "latitud",
        "longitud"
    )

    return JsonResponse({
        "status": 200,
        "ubicaciones": list(ubicaciones)
    })

@csrf_exempt
def inserta_ubicacion(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            nueva = ubicacion.objects.create(
                latitud=data["latitud"],
                longitud=data["longitud"]
            )

            return JsonResponse({
                "status": 201,
                "id_ubi": nueva.id_ubi
            })

        except Exception as ex:
            return JsonResponse({
                "status": 400,
                "error": str(ex)
            }, status=400)

    return JsonResponse({
        "status": 405,
        "mensaje": "Método no permitido"
    }, status=405)