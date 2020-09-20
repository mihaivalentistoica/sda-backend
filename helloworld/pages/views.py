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
    return HttpResponse('Eu sunt pagina 1, bine ai venit!')


def page2(request):
    return HttpResponse('Eu sunt a doua pagina.')
