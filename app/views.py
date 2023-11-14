from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# todas as páginas

def index(request):
    return render(
        request,
        'app/index.html'
    )

def estagios(request):
    return render(
        request,
        'app/estagios.html'
    )


def cursos(request):
    return render(
        request,
        'app/cursos.html'
    )

def about(request):
    return render(
        request,
        'app/about.html'
    )

def como_ingressar(request):
    return render(
        request,
        'app/como_ingressar.html'
    )

def galeria(request):
    return render(
        request,
        'app/galeria.html'
    )

def contato(request):
    return render(
        request,
        'app/contato.html'
    )

