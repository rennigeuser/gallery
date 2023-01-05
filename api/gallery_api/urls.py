from django.urls import path, include
from . import views

app_name = 'gallery_api'

urlpatterns = [
    path('v1/', include([
        path('posts/', include([
            path('', views.post_list, name='post_list'),
            path('create/', views.post_create, name='post_create'),
            path('<int:pk>/', include([
                path('', views.post_detail, name='post_detail'),
                path('delete/', views.post_delete, name='post_delete'),
            ])),
        ])),
        path('images/', include([
            path('', views.image_list, name='image_list'),
        ])),
    ])),
]