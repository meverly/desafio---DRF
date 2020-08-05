from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from aplicativo.models import Afazeres
from aplicativo.serializers import AfazeresSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class AfazeresViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Afazeres.objects.all()
    serializer_class = AfazeresSerializer

class AfazeresList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Afazeres.objects.all()
    serializer_class = AfazeresSerializer 

class AfazeresRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Afazeres.objects.all()
    serializer_class = AfazeresSerializer    