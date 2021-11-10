from django.urls import path
from .views import *
 
urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user'),

]