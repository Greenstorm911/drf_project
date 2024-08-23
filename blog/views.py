from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .serializers import *
from django.contrib.auth.models import User
from .models import Blog
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import BlocklistPermission



@api_view(['GET', 'POST'])
def hello(request):
    
    print(request.META['REMOTE_ADDR'])
    return Response({'message': 'hello, world!'})

class class_base_view(APIView):
    def get(self, request):
        name = request.GET.get('name')
        # data = request.data
        # data['name']
        # data.get('name')
        return Response({"message": 'hello {name}'})

    def post(self, request):
        return Response({"message": 'class base view POST'})

class Game(APIView):
    def get(self, request):
        # url = "https://api.truthordarebot.xyz/api/"
        # game_type = request.GET.get('game')
        # response = requests.get('https://api.truthordarebot.xyz/api/' + game_type)
        # response = response.json()
        # result = {
        #     'game': response['type'],
        #     'question' : response['question']
        # }
        users = User.objects.all()
        ser = UserSerializer(instance=users, many=True)
        return Response(data=ser.data)

class Blog_view(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        ser = BlogSerializer(instance=blog)
        return Response(data=ser.data)
from rest_framework.permissions import IsAuthenticated
class Blog_add_view(APIView):
    permission_classes = [IsAuthenticated, BlocklistPermission]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        serializers = BlogSerializer(data=request.data)
        if serializers.is_valid():
            if request.user.is_authenticated:
                serializers.validated_data['user'] = request.user
            serializers.save()
            return Response({'status': 'done', 'data': serializers.data }, status=status.HTTP_201_CREATED)
        return Response({'status': serializers.errors})


class BlogAddView2(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        # for sending the request and then useing the request in the serializer 
        serializers = BlogSerializer(data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'done', 'data': serializers.data }, status=status.HTTP_201_CREATED)
        return Response({'status': serializers.errors})







class BlogUpdateView(APIView):
    def put(self, request, pk):
        instance = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'done', 'data': serializer.data })
        else:
            return Response({'status': serializer.errors})

    def delete(self, request, pk):
        instance = Blog.objects.get(pk=pk)
        instance.delete()
        return Response({'status': 'deleted'})


class BlogUpdateView2(APIView):
    def put(self, request, pk):
        instanace = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(instanace=instanace, validated_data=serializer.validated_data)
            return Response({'status': 'done', 'data': serializer.data })
        else:
            return Response({'status': serializer.errors})

    def delete(self, request, pk):
        instance = Blog.objects.get(pk=pk)
        instance.delete()
        return Response({'status': 'deleted'})


from rest_framework.authentication import TokenAuthentication
class CheckToken(APIView):
    # if not define in setting this has to define for each class
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        user = request.user
        return Response({'user': user.username}, status=status.HTTP_200_OK)