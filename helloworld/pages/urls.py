from django.urls import path
from .views import home, page1, page2

app_name = 'pages'
urlpatterns = [
    path('', home, name='home'),
    path('page1', page1, name='page1'),
    path('page2', page2, name='page2'),
]
