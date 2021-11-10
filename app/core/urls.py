from django.urls import path
from .views import *


 
urlpatterns = [
    path('state/', StateListView.as_view(), name='state_list'),
    path('state/<int:pk>/', StateDetailView.as_view(), name='state'),

    path('case/', CaseListView.as_view(), name='case_list'),
    path('case/<int:pk>/', CaseDetailView.as_view(), name='case'),

    path('portfolio/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio/<int:pk>/', PorfolioDetailView.as_view(), name='portfolio'),

    path('sessions/', SessionsListView.as_view(), name='sessions_list'),
    path('sessions/<int:pk>/', SessionsDetailView.as_view(), name='sessions'),

]