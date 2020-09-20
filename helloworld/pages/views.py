from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('Hello, world!')


def page1(request):
    return HttpResponse('Eu sunt pagina 1, bine ai venit!')


def page2(request):
    return HttpResponse('Eu sunt a doua pagina.')
