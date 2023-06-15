from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializers import BookCollectionSerializer
import datetime


class BooksCollectionApiView(APIView):
    
    #1. List all
    def get(self, *args, **kwargs):
        books = Books.objects.all()
        serializer = BookCollectionSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #2. Create
    def post(self, request, *args, **kwargs):
        '''Creating Books collection with given book data'''
        data = {
            'title' : request.data.get('title'),
            'author' : request.data.get('author'),
            'publication_year' : request.data.get('publication_year'),
        }
        serializer = BookCollectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)