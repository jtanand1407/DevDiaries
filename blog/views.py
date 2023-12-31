from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def post_list(request, format=None):

    if request.method == 'GET':
        try:
            posts=Post.objects.all()
            serializer=PostSerializer(posts,many=True)
            return Response({"posts": serializer.data},status=status.HTTP_200_OK)
        except Exception as ex:
            return JsonResponse({'error_message': ex},status=status.HTTP_400_BAD_REQUEST)

    
     
    if request.method == 'POST':
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def post_detail(request,id, format=None):
    try:
        post=Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer=PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
