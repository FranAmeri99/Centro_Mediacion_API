from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict


class UsersListView(View):
    def get(self, request):
        if('name' in request.GET):
            rlist = User.objects.filter(name__contains=request.GET['name'])
        else:
            rlist = User.objects.all()
        return JsonResponse(list(rlist.values()), safe=False)

class UserDetailView(View):
    def get(self, request, pk):
        resolution = User.objects.get(pk=pk)
        return JsonResponse(model_to_dict(resolution))
