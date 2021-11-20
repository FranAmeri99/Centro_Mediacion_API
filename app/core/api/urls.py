from django.urls import path

from core.api.api import *
from core.views import *
urlpatterns = [
    
    path('state/', state_api_view, name='state'),
    path('case/', case_api_view, name='case'),
    path('portafolio/', portafolio_api_view, name='portafolio'),
    path('sessions/', sessions_api_view, name='sessions'),
    path('state/<int:pk>/', state_detail_api_view, name='state_detail'),
    path('case/<int:pk>/', case_detail_api_view, name='case_detail'),
    path('portafolio/<int:pk>/', portfolio_detail_api_view, name='portafolio_detail'),
    path('sessions/<int:pk>/', session_detail_api_view, name='sessions_detail')
]
