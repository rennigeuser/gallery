from django.urls import path, include

urlpatterns = [
    path('gallery/', include('api.gallery_api.urls')),
]
