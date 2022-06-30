from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import Curso

def saludo(request):
    fecha_hora_ahora=datetime.now()
    return HttpResponse(f"Hola mundo {fecha_hora_ahora}")

def saludar_a(request,nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")

def mostrar_mi_template(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]
        
    return render(request,"mi_app/index.html",context)

def listar_cursos(request):
    context={}
    context["cursos"] = Curso.objects.all()
    return render(request, "mi_app/lista_cursos.html",context)
