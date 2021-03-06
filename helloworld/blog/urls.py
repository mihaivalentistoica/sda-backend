from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.blog_post_list, name='home'),
    path('<int:post_id>/', views.blog_post_details, name='blog_post_details'),
]
