from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializers import BookCollectionSerializer
import datetime


class BooksCollectionApiView(APIView):
    
    #1. List Books Collection
    def get(self, *args, **kwargs):
        books = Books.objects.all()
        serializer = BookCollectionSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #2. Create Book Record
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
    
class BooksCollectionDetailApiView(APIView):
    def get_book_object(self, book_id):
        try:
            return Books.objects.get(id=book_id)
        except Books.DoesNotExist:
            return None
        
    #3. Retrieve Book Record
    def get(self, request, book_id, *args, **kwargs):
        book_instance = self.get_book_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = BookCollectionSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #4. Update Book Record
    def put(self, request, book_id, *args, **kwargs):
        book_instance = self.get_book_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        data = {
            'title' : request.data.get('title'),
            'author' : request.data.get('author'),
            'publication_year' : request.data.get('publication_year'),
        }
        serializer = BookCollectionSerializer(instance=book_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    #5. Delete Book Record
    def delete(self, request, book_id, *args, **kwargs):
        book_instance = self.get_book_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        book_instance.delete()
        return Response(
            {"res" : "Book record successfully deleted!"},
            status = status.HTTP_204_NO_CONTENT
        )