from django.urls import path
from .views import *
 
urlpatterns = [
    path('resolution/', ResolutionListView.as_view(), name='resolution_list'),
    path('resolution/<int:pk>/', ResolutionDetailView.as_view(), name='resolution'),
]