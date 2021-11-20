from core.models import *
from core.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status

from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def state_api_view(request):
    if request.method == 'GET':
        state = State.objects.all()
        stateSerializers = StateSerializers(state, many=True)
        return Response(stateSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        stateSerializers = StateSerializers(data = request.data)
        if stateSerializers.is_valid():
            stateSerializers.save()
            return Response(stateSerializers.data, status.HTTP_201_CREATED)
        return Response(stateSerializers.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])

def case_api_view(request):
    if request.method == 'GET':
        case = Case.objects.all()
        caseSerializers = CaseSerializers(case, many=True)
        return Response(caseSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        caseSerializers = CaseSerializers(data = request.data)
        if caseSerializers.is_valid():
            caseSerializers.save()
            return Response(caseSerializers.data, status.HTTP_201_CREATED)
        return Response(caseSerializers.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def portafolio_api_view(request):
    if request.method == 'GET':
        portafolio = MediationPortafolio.objects.all()
        portafolioSerializers = PortafolioSerializers(portafolio, many=True)
        return Response(portafolioSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        portafolio = PortafolioSerializers(data = request.data)
        if portafolio.is_valid():
            portafolio.save()
            return Response(portafolio.data, status.HTTP_201_CREATED)
        return Response(portafolio.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def sessions_api_view(request):
    if request.method == 'GET':
        sessions = MediationSessions.objects.all()
        sessionsSerializers = SessionsSerializers(sessions, many=True)
        return Response(sessionsSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        sessions = SessionsSerializers(data = request.data)
        if sessions.is_valid():
            sessions.save()
            return Response(sessions.data, status.HTTP_201_CREATED)
        return Response(sessions.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def state_detail_api_view(request, pk=None):
    state = State.objects.filter(id = pk).first()
    if state:
        if request.method == 'GET':
            stateSerializers = StateSerializers(state)
            return Response(stateSerializers.data, status.HTTP_200_OK)

        elif request.method == 'PUT':
            stateSerializers = StateSerializers(state, data = request.data)
            if stateSerializers.is_valid():
                stateSerializers.save()
                return Response(stateSerializers.data)
            return Response(stateSerializers.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            state.delete()
            return Response('Eliminado')

    return Response({'message:':'No se a encontrado un estado con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def case_detail_api_view(request, pk=None):
    case = Case.objects.filter(id = pk).first()
    if case:
        if request.method == 'GET':
            caseSerializers = CaseSerializers(case)
            return Response(caseSerializers.data, status.HTTP_200_OK)

        elif request.method == 'PUT':
            caseSerializers = CaseSerializers(case, data = request.data)
            if caseSerializers.is_valid():
                caseSerializers.save()
                return Response(caseSerializers.data)
            return Response(caseSerializers.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            case.delete()
            return Response('Eliminado')

    return Response({'message:':'No se a encontrado un caso con estos datos'})

@api_view(['GET', 'PUT', 'DELETE'])
def portfolio_detail_api_view(request, pk=None):
    portafolio = MediationPortafolio.objects.filter(id = pk).first()
    if portafolio:
        if request.method == 'GET':
            portafolioSerializers = PortafolioSerializers(portafolio)
            return Response(portafolioSerializers.data, status.HTTP_200_OK)

        elif request.method == 'PUT':
            portafolioSerializers = PortafolioSerializers(portafolio, data = request.data)
            if portafolioSerializers.is_valid():
                portafolioSerializers.save()
                return Response(portafolioSerializers.data)
            return Response(portafolioSerializers.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            portafolio.delete()
            return Response('Eliminado')

    return Response({'message:':'No se a encontrado un portfolio con estos datos'}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def session_detail_api_view(request, pk=None):
    session = MediationSessions.objects.filter(id = pk).first()
    if session:
        if request.method == 'GET':
            sessionSerializers = SessionsSerializers(session)
            return Response(sessionSerializers.data, status.HTTP_200_OK)

        elif request.method == 'PUT':
            sessionSerializers = SessionsSerializers(session, data = request.data)
            if sessionSerializers.is_valid():
                sessionSerializers.save()
                return Response(sessionSerializers.data)
            return Response(sessionSerializers.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            session.delete()
            return Response('Eliminado')

    return Response({'message:':'No se a encontrado una  Session con estos datos'})
