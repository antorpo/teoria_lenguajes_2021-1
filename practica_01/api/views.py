from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CadenaSerializer
from .models import Cadena

from .token_functions import tokenizador 

# Obtener la ultima cadena ingresada
@api_view(['GET'])
def cadenaList(request):
	cadenas = Cadena.objects.all().order_by('-id')
	serializer = CadenaSerializer(cadenas, many=True)
	return Response(serializer.data)

# Crear cadenas
@api_view(['POST'])
def cadenaCreate(request):
	serializer = CadenaSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# Borrar cadenas
@api_view(['DELETE'])
def cadenaDelete(request, pk):
	cadena = Cadena.objects.get(id=pk)
	cadena.delete()

	return Response('Item succesfully delete!')


@api_view(['DELETE'])
def cadenaDeleteFirst(request):
	cadena = Cadena.objects.first()
	cadena.delete()

	return Response('Item succesfully delete!')


@api_view(['DELETE'])
def cadenaDeleteAll(request):
	cadena = Cadena.objects.all()
	cadena.delete()

	return Response('Item succesfully delete!')


# Traer ultima cadena, tambien se puede la primera .first()
@api_view(['GET'])
def cadenaLast(request):
	cadenas = Cadena.objects.last()
	serializer = CadenaSerializer(cadenas, many=False)
	return Response(serializer.data)
	

@api_view(['GET'])
def tokenArray(request):
	cadena = Cadena.objects.first()
	response = tokenizador.tokens_to_Json(cadena.secuencia)
	return Response(response)



