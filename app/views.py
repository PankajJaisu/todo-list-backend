from django.shortcuts import render
from .serializers import *
from django.http import JsonResponse
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes

# Create your views here.


"""
We are Using ClassBased View as we are having different HTTP method to use on same model,
so class Based View Provide More Readibility,Reusability in such Cases
"""

@api_view(['POST'])
def add_tag(request):
    if request.data!={}:
        for i in request.data:
            Tag.objects.create(name=i['name'])
        return JsonResponse({"message":"Tag Added Successfully"},status=status.HTTP_201_CREATED)           
    else:
        return JsonResponse({"message":"Please Provide Name for Tag"},status=status.HTTP_400_BAD_REQUEST)          
    

@api_view(['POST'])
def add_task(request):
    data = request.data 
    task_serializer = TaskSerializer(data=data)  
    if task_serializer.is_valid():
        task_serializer.save()
        return JsonResponse({"message":"New Task Added Successfully","data":task_serializer.data},status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({"error":task_serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class TaskView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
   
    def get(self,request,id):
        task_queryset = Task.objects.filter(id=id)
        if len(task_queryset)>0:
            print(task_queryset)
            response_data = TaskSerializer(task_queryset.last()).data
            return JsonResponse({"message":"Data Fetched Successfully for Task {}".format(id),"data":response_data},status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message":"Task Not Found"},status=status.HTTP_404_FOUND)

    def put(self,request,id):
        task_queryset = Task.objects.filter(id=id)
        if len(task_queryset)>0:
            task_serializer = TaskSerializer(instance=task_queryset.last(),data=request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return JsonResponse({"message":"Task {} updated Successfully".format(id),"data":task_serializer.data},status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error":task_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"message":"Task Not Found with {} Id"}.format(id),status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        task_queryset = Task.objects.filter(id=id)
        if len(task_queryset)>0:
            task_queryset.delete()
            return JsonResponse({"message":"Task {} deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({"message":"Task Not Found"},status=status.HTTP_404_NOT_FOUND)


# API to get all Task Data ,we will use Function based View here for its simplicity 

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_all_task(request):
    print("request.user::",request.user)
    all_task = Task.objects.all()
    if len(all_task)>0:
        response_data = Task.objects.all().values()
        return JsonResponse({"message":"All Data Fetched Successfully","data":list(response_data)},status=status.HTTP_200_OK)
    else:
        return JsonResponse({"message":"No Task Found"},status=status.HTTP_404_NOT_FOUND)
