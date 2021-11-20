from django.urls import path
from Resolution.views import *
from Resolution.api.api import *
urlpatterns = [
    path('portfolio/', resolution_portfolio_api_view, name='resolution_portfolio'),
    path('session/', resolution_session_api_view, name='resolution_session'),
    path('portfolio/<int:pk>/', resolution_portfolio_detail_api_view, name='resolution_portfolio'),
    path('session/<int:pk>/', resolution_session_detail_api_view, name='resolution_session'),

]
