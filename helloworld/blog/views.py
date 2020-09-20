from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

blog_entries = [
    {
        'id': 1,
        'title': 'Hello, world!',
        'body': 'I have created my first template in Django!'
    },
    {
        'id': 2,
        'title': 'A title',
        'body': 'And a description.'
    },
    {
        'id': 3,
        'title': 'Hello, world 2 !',
        'body': 'I have created my first template in Django!'
    },
    {
        'id': 4,
        'title': 'A title 2 ',
        'body': 'And a description.'
    },
    {
        'id': 5,
        'title': 'Hello, world 3 !',
        'body': 'I have created my first template in Django!'
    },
    {
        'id': 6,
        'title': 'A title 3',
        'body': 'And a description.'
    }
]


def get_post_by_id(post_id):
    for post in blog_entries:
        if post['id'] == post_id:
            return post


# Create your views here.

def blog_post_list(request):
    context = {
        'blog_entries': blog_entries
    }

    return render(request, 'blog_post.html', context=context)


def blog_post_details(request, post_id):
    post = get_post_by_id(post_id)
    if not post:
        return HttpResponseNotFound('<h1>Blog post not found</h1>')
    return render(request, 'blog_post_details.html', {'post': post})
