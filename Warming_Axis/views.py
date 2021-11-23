from django.shortcuts import render

def Inicio(request):
    return render(request, "Inicio.html")

def noticias(request):
    return render(request, "noticias.html")

def foros(request):
    return render(request, "foros.html")

def informacion(request):
    return render(request, "informacion.html")

def acerca(request):
    return render(request, "acerca_de.html")