from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import taskSerializer


@api_view(['GET'])
def lista_tarefas(request):
    tarefas = Task.objects.all()
    lista_tarefas = list(tarefas.values)
    lista_serializada = taskSerializer(lista_tarefas, many=True)
    return Response(lista_serializada.data)


def Tasks(request):
    
    if request.method == 'GET':
        tarefas = Task.objects.all()
        lista_tarefas = list(tarefas.values)
        lista_serializada = taskSerializer(lista_tarefas, many=True)
        return Response(lista_serializada.data)
    

