from .models import Perro
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import perroSerializer
from django.shortcuts import render


class ListaPerros(APIView):


    def get(self,request):
        perros  = Perro.objects.all()
        serializer = perroSerializer(perros,context={"request":request},many=True)#El many true es porque donde extreamos varias fields son atributos del objectofield
                                                    #sino se pone true este extrae solo un objeto y nosotros estamos extrayendo varios objectos iterables
                                                    
        return Response(serializer.data) 
    def post(self,request):
        pass                                                