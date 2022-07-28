from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from majorproject.serializers import FileSerializer

# Create your views here.

@api_view(['POST'])
def file_upload(request):
    if request.method=='POST':
        file=request.FILES['file']

        print(file)
        data={
            'file':file
        }
        file_serializer=FileSerializer(data=data)
        if file_serializer.is_valid():
            file_serializer.save()

            return JsonResponse(file_serializer.data,status=status.HTTP_201_CREATED)

        return JsonResponse(file_serializer.errors,status=status.HTTP_400_BAD_REQUEST)