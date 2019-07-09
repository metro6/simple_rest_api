from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer

from authors.models import Author
from authors.serializers import AuthorSerializer

@api_view(['GET'])
def get_books(request):
    serializer = BookSerializer(Book.objects.all(), many=True)
    return Response({'books': serializer.data}, status=200)


@api_view(['GET'])
def get_book(request, id):
    serializer = BookSerializer(Book.objects.filter(pk=id), many=True)
    return Response({'books': serializer.data}, status=200)



@api_view(['GET'])
def get_authors(request):
    serializer = AuthorSerializer(Author.objects.all(), many=True)
    return Response({'authors': serializer.data}, status=200)@api_view(['GET'])


@api_view(['GET'])
def get_author(request, id):
    serializer = AuthorSerializer(Author.objects.filter(pk=id), many=True)
    return Response({'authors': serializer.data}, status=200)