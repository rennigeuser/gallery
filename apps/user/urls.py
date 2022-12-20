from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
	path('', views.start_page, name='startpage'),
	path('registration/', views.register_user, name='registration'),
]

