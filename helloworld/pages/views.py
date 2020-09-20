from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    context = {
        'username': 'Stoica Mihai',
        'section': {
            'title': 'My first page'
        },
        'breakfast': [
            'milk',
            'coffee',
            'bacon',
            'egs'
        ]
    }
    return render(request=request, template_name='home.html', context=context)


def page1(request):
    return render(request=request, template_name='page1.html')


def page2(request):
    return render(request=request, template_name='page2.html')
