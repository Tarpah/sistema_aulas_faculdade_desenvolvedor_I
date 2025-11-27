from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from services.serializers import CalculoSerializer


@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao": "Olá mundo"})

class ExemploSaudacao(APIView):
    def get(self, request):
        return Response({"saudacao": "Olá Mundo em classe"})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'saudacao': reverse('services:saudacao', request=request, format=format),
    })

@api_view(['GET','POST'])
def calculo(request):
    try:
        if request.method == 'GET':
            serializer = CalculoSerializer()
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            dados = JSONParser().parse(request)
            serializer = CalculoSerializer(data=dados)
            if serializer.is_valid():
                serializer.calcular()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        context = {
            "error": str(e)
        }
        return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST, safe=False)