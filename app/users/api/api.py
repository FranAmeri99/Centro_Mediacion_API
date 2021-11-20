from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.models import Token

from users.models import User
from users.api.serializers import UserSerializers, UserListSerializers
#from users.permissions.permissions import UpdateOwnProfile

@api_view(['GET', 'POST'])
def users_api_view(request):
    if request.method == 'GET':
        users = User.objects.all().values('id','password','is_superuser','enrollment','dni','username','email','name','last_name', 'is_staff')
        userSerializers = UserListSerializers(users, many=True)
        return Response(userSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        userSerializers = UserSerializers(data = request.data)
        if userSerializers.is_valid():
            userSerializers.save()
            return Response(userSerializers.data)
        return Response(userSerializers.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail_api_view(request, pk=None):
    users = User.objects.filter(id = pk).first()
    if users:
        if request.method == 'GET':
            userSerializers = UserSerializers(users)
            return Response(userSerializers.data, status.HTTP_200_OK)

        elif request.method == 'PUT':
            userSerializers = UserSerializers(users, data = request.data)
            if userSerializers.is_valid():
                userSerializers.save()
                return Response(userSerializers.data)
            return Response(userSerializers.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            users.delete()
            return Response('Eliminado')
    return Response({'message:':'No se a encontrado un usario con estos datos'})
