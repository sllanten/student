from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
#  return HttpResponse('!Hola desde Django!')
    guest = {
        'nombre': 'Jaime Alexander Jurado Lopez',
        'materia': 'Electiva 5',
    }
    perso1 = {
        'id': 1,
        'nombre': 'Juan Andrés Pérez Gómez',
        'codigo': 6789012345,
    }
    perso2 = {
        'id': 2,
        'nombre': 'María Laura Rodríguez López',
        'codigo': 1478523698,
    }

    perso3 = {
        'id':3,
        'nombre': 'Catalina Valentina Torres Ramírez',
        'codigo': 3456789012,
    }
    perso4 = {
        'id':4,
        'nombre': 'STIVEN RONJA',
        'codigo': 323678912,
    }
    
    return render(request, 'index.html',{'login': guest,'dt1': perso1,'dt2': perso2,'dt3': perso3,'dt4': perso4})
