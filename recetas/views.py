from django.shortcuts import render

from .repository import obtener_receta


def index(request):
    receta = obtener_receta()
    return render(request, "recetas/index.html", {"receta": receta})
