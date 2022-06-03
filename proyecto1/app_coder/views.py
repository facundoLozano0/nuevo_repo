from colorama import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import curso
# Create your views here.

def cursos(request):
    cursos=curso.objects.all()
    return HttpResponse(cursos)

def alta_curso(request,nombre):
    cursoo=curso(nombre=nombre, camada=21315)
    cursoo.save()
    texto=f' curso:{cursoo.nombre} camada:{cursoo.camada} '
    return HttpResponse(texto)



