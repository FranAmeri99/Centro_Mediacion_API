from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict

class ResolutionListView(View):
    def get(self, request):
        if('resolution' in request.GET):
            rlist = Resolution.objects.filter(description__contains=request.GET['resolution'])
        else:
            rlist = Resolution.objects.all()
        return JsonResponse(list(rlist.values()), safe=False)

class ResolutionDetailView(View):
    def get(self, request, pk):
        resolution = Resolution.objects.get(pk=pk)
        return JsonResponse(model_to_dict(resolution))
