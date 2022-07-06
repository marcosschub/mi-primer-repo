from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import Curso

def saludo(request):
    fecha_hora_ahora=datetime.now()
    return HttpResponse(f"Hola mundo {fecha_hora_ahora}")

def saludar_a(request,nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")

def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo":"Este es mi primer website!!!"})


def listar_cursos(request):
    context={}
    context["cursos"] = Curso.objects.all()
    return render(request, "mi_app/lista_cursos.html",context)
