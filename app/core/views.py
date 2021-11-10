from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from rest_framework.views import APIView

class StateListView(APIView):
    def get(self, request):
        if('description' in request.GET):
            slist = State.objects.filter(description__contains=request.GET['description'])
        else:
            slist = State.objects.all()
        return JsonResponse(list(slist.values()), safe=False)
        
class StateDetailView(View):
    def get(self, request, pk):
        state = State.objects.get(pk=pk)
        return JsonResponse(model_to_dict(state))

class CaseListView(View):
    def get(self, request):
        if('name' in request.GET):
            slist = Case.objects.filter(name__contains=request.GET['name'])
        else:
            slist = Case.objects.all()
        return JsonResponse(list(slist.values()), safe=False)
        
class CaseDetailView(View):
    def get(self, request, pk):
        case = Case.objects.get(pk=pk)
        return JsonResponse(model_to_dict(case))

class PortfolioListView(View):
    def get(self, request):
        if('name' in request.GET):
            slist = MediationPortafolio.objects.filter(name__contains=request.GET['name'])
        else:
            slist = MediationPortafolio.objects.all()
        return JsonResponse(list(slist.values()), safe=False)
        
        
class PorfolioDetailView(View):
    def get(self, request, pk):
        portfolio = MediationPortafolio.objects.get(pk=pk)
        return JsonResponse(model_to_dict(portfolio))

class SessionsListView(View):
    def get(self, request):
        slist = MediationSessions.objects.all()
        return JsonResponse(list(slist.values()), safe=False)
        
class SessionsDetailView(View):
    def get(self, request, pk):
        sessions = MediationSessions.objects.get(pk=pk)
        return JsonResponse(model_to_dict(sessions))
