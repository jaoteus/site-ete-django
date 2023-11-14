# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# todas as páginas

def home(request):
    return HttpResponse('home do app')