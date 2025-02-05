from rest_framework import generics, permissions, reverse
from .models import Fabricante, Tag, Ativo, Setor
from ativos.serializers import FabricanteSerializer, TagSerializer, AtivoSerializer, SetorSerializer
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



class FabricanteListCreateView(generics.ListCreateAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer


class FabricanteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AtivoListCreateView(generics.ListCreateAPIView):
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer


class AtivoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
    

class SetorListCreateView(generics.ListCreateAPIView):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class SetorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
