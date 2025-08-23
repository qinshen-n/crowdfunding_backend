from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )

class CustomUserDetail(APIView):
    def get_object(self, pk): # a helper method to retrieve a signle CustomUser instance from the database
        try: # try ... expect: error handling
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk): # main view method to handle the HTTP GET request
        user = self.get_object(pk) # call the get_object helper method to get the data
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)