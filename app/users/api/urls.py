from django.urls import path

from users.api.api import *
urlpatterns = [
    path('usuarios/', users_api_view, name='usuarios'),
    path('usuarios/<int:pk>/', users_detail_api_view, name='usuarios_pk)')
]
