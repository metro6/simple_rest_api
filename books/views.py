import json

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from .models import Book
from authors.models import Author


class BookView(View):

  def post(self, request):
    if request.method == 'POST':
      name = request.POST.get('name')
      try:
        author = Author.objects.get(request.POST.get('author'))

      except:
        response = {
          'status': 'error',
          'message': 'Author not found'
        }
        return HttpResponse(json.dumps(response))
      book = Book.objects.get_or_create(name=name, author=author)
      response = {'status': 'success',
                  'message': 'logged in',
                  'book': book}
      return HttpResponse(json.dumps(response))

  def get(self, request):
    if request.method == 'GET':
      template = 'books/books.pug'
      books = Book.objects.all()
      return render(request, template, {'books': books})


def get_books(request, id):
  book = Book.objects.filter(pk=id).first()
  template = 'books/book.pug'
  return render(request, template, {'book': book})
