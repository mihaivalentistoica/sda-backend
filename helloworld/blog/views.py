from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog_post(request):
    return HttpResponse('Eu sunt un blog post')