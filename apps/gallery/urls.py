from django.urls import path, include
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.main_page , name='start_page'),
    path('getPosts/', views.get_posts, name='get_posts'),
]
