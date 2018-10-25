from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class UserTaskView(APIView):
    def post(self, request):
        request.data['user'] = request.user.id
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        task_status = request.GET.get('status')
        if task_status:
            status_tasks = request.user.tasks.filter(status=task_status)
            serializer = TaskSerializer(status_tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        pending_tasks = request.user.tasks.filter(status="PENDING")
        completed_tasks = request.user.tasks.filter(status="COMPLETED")
        p_serializer = TaskSerializer(pending_tasks, many=True)
        c_serializer = TaskSerializer(completed_tasks, many=True)
        return Response({"completed": c_serializer.data, "pending": p_serializer.data}, status=status.HTTP_200_OK)



class TaskView(APIView):

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        if task.user != request.user:
            return Response({'error': 'User is not authorized to perform action'}, status=status.HTTP_401_UNAUTHORIZED)

        request.data['user'] = request.user.id
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        if task.user != request.user:
            return Response({'error': 'User is not authorized to perform action'}, status=status.HTTP_401_UNAUTHORIZED)

        task.delete()
        return Response({'msg': 'succesfully deleted'}, status=status.HTTP_200_OK)

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        if task.user != request.user:
            return Response({'error': 'User is not authorized to perform action'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


        
