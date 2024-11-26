from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def apiShow(request):
    dataStudent = [
        {"id": 1, "nombre": "Juan Andrés Pérez Gómez","codigo": 6789012345},
        {"id": 2, "nombre": "María Laura Rodríguez López","codigo": 1478523698},
        {"id": 3, "nombre": "Catalina Valentina Torres Ramírez","codigo": 3456789012},
        {"id": 4, "nombre": "Stiven Ronja'","codigo": 3456789012},
    ]
    return JsonResponse(dataStudent, safe=False)

def index(request):
    guest = {
        'nombre': 'Jaime Alexander Jurado Lopez',
        'materia': 'Electiva 5',
    }

    return render(request, 'index.html',{'login': guest})