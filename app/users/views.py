from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.sessions.models import Session

from users.api.serializers import TokenSerializer
from datetime import datetime

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            print (user.username)
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializar = TokenSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user': user_serializar.data,
                        'messaje': 'Inicio de session exitosa'
                    }, status= status.HTTP_201_CREATED)
                else:
                    all_session = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                                """Cierra las sessiones si genera otro token """
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token':token.key,
                        'user': user_serializar.data,
                        'messaje': 'Inicio de session exitosa'
                    }, status= status.HTTP_201_CREATED)

            else:
                return Response({'messaje':'el usuario no esta activo, no puede iniciar session'},
                status = status.HTTP_401_UNAUTHORIZED )

        else:
            return Response({'messaje':'Usuario o contraseña incorrecta'},status = status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.POST.get('token')
            token = Token.objects.filter(key=token).first()

            if token:
                user = token.user
                all_session = Session.objects.filter(expire_date__gte=datetime.now())
                if all_session.exists():
                    for session in all_session:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_msm = 'Session del usuario eliminada'
                token_msm = 'Toke eliminado'

                return Response({'token_message':token_msm, 'session_message':session_msm}, status= status.HTTP_200_OK)
            return Response({'error':'no se encontro usuario con este token'}, status= status.HTTP_400_BAD_REQUEST)
        except:
            #no anda
            return Response({'error': 'token no valido'}, status= status.HTTP_409_CONFLICT)
