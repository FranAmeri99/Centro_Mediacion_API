from rest_framework.views import APIView
from rest_framework import status
from Resolution.models import *
from Resolution.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def resolution_portfolio_api_view(request):
    if request.method == 'GET':
        resolution_portfolio = ResolutionPortfolio.objects.all()
        resolution_portfolioSerializers = ResolutionPortfolioSerializers(resolution_portfolio, many=True)
        return Response(resolution_portfolioSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        resolution_portfolioSerializers = ResolutionPortfolioSerializers(data = request.data)
        if resolution_portfolioSerializers.is_valid():
            resolution_portfolioSerializers.save()
            return Response(resolution_portfolioSerializers.data, status.HTTP_201_CREATED)
        return Response(resolution_portfolioSerializers.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def resolution_session_api_view(request):
    if request.method == 'GET':
        resolution = ResolutionSession.objects.all()
        resolutionSerializers = ResolutionSessionSerializers(resolution, many=True)
        return Response(resolutionSerializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        resolutionSerializers = ResolutionSessionSerializers(data = request.data)
        if resolutionSerializers.is_valid():
            resolutionSerializers.save()
            return Response(resolutionSerializers.data, status.HTTP_201_CREATED)
        return Response(resolutionSerializers.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def resolution_portfolio_detail_api_view(request, pk=None):
    resolution = ResolutionPortfolio.objects.filter(id = pk).first()
    if resolution:
        if request.method == 'GET':
            resolutionPortfolioSerializers = ResolutionPortfolioSerializers(resolution)
            return Response(resolutionPortfolioSerializers.data, status.HTTP_200_OK )

        elif request.method == 'PUT':
            resolution = ResolutionPortfolio.objects.filter(id = pk).first()
            resolutionPortfolioSerializers = ResolutionPortfolioSerializers(resolution, data = request.data)
            if resolutionPortfolioSerializers.is_valid():
                resolutionPortfolioSerializers.save()
                return Response(resolutionPortfolioSerializers.data, status.HTTP_201_CREATED)
            return Response(resolutionPortfolioSerializers.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            resolution = ResolutionPortfolio.objects.filter(id = pk).first()
            resolution.delete()
            return Response('Eliminado')

    return Response({'message:':'No se a encontrado una resolucion de Portafolio con estos datos'})

@api_view(['GET', 'PUT', 'DELETE'])
def resolution_session_detail_api_view(request, pk=None):
    resolution = ResolutionSession.objects.filter(id = pk).first()
    if resolution:
        if request.method == 'GET':
            resolutionSessionSerializers = ResolutionSessionSerializers(resolution)
            return Response(resolutionSessionSerializers.data, status.HTTP_200_OK)

        elif request.method == 'PUT':
            resolutionSessionSerializers = ResolutionSessionSerializers(resolution, data = request.data)
            if ResolutionSessionSerializers.is_valid():
                ResolutionSessionSerializers.save()
                return Response(ResolutionSessionSerializers.data, status.HTTP_201_CREATEDS)
            return Response(ResolutionSessionSerializers.errors,status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            resolution.delete()
            return Response('Eliminado')

    return Response({'message:':'No se a encontrado una resolucion de Session con estos datos'})
