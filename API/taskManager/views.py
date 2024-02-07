from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import taskSerializer


@api_view(['GET'])
def lista_tarefas(request):
    tarefas = Task.objects.all()
    lista_tarefas = list(tarefas.values)
    lista_serializada = taskSerializer(lista_tarefas, many=True)
    return Response(lista_serializada.data)

@api_view(['GET','POST','DELETE','PUT'])
def Tasks(request):
    
    if request.method == 'GET':
        try:
            tarefas = Task.objects.all()
            lista_tarefas = list(tarefas.values)
            lista_serializada = taskSerializer(lista_tarefas, many=True)
            return Response(lista_serializada.data)
        except Exception as excecao:
            print("aaaaaaaaaaaa")
            return Response("Não foi possível retornar as tarefas: ",excecao)
    elif request.method == 'POST':
        try :
            nova_tarefa = taskSerializer(data=request.data)
            if nova_tarefa.is_valid():
                nova_tarefa.save()
                print("Uma nova tarefa foi criada: ",nova_tarefa.data)
                return Response(200)
            else:
                print("Os dados inseridos são invalidos")
                raise Exception(500)
        except Exception as e:
            print("Ocorreu um erro: ",e)
            return Response(500)
    elif request.method == "DELETE":
        try:
            tarefa_to_delete = Task.objects.get(id=request.data['id'])
            tarefa_to_delete.delete()
            print("Tarefa deletada com sucesso")
            return Response(200)
        except Exception as e:
            print("Ocorreu um erro: ",e)
            return Response(500)
                
    elif request.method == "PUT":
        try:
            tarefa_to_update = Task.objects.get(id=request.data['id'])
            tarefa_to_update_serialized = taskSerializer(tarefa_to_update, data=request.data)
            
            if tarefa_to_update_serialized.is_valid():
                tarefa_to_update_serialized.save()
                print("Tarefa Atualizada")
                return Response(200)
                

        except Exception as e:
            print("Ocorreu um erro: ",e)
            return Response(500)