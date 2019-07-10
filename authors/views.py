import json

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from .models import Author
from books.models import Book

class AuthorView(View):

  def post(self, request):
    if request.method == 'POST':
      name = request.POST.get('name')
      author = Author.objects.get_or_create(name=name)
      response = {'status': 'success',
                  'message': 'author created',
                  'author': author}
      return HttpResponse(json.dumps(response))

  def get(self, request):
    if request.method == 'GET':
      template = 'authors/authors.pug'
      authors = Author.objects.all()
      return render(request, template, {'authors': authors})


def get_authors(request, id):
  author = Author.objects.filter(pk=id).first()
  books_filter = Book.objects.filter(author=author)
  books = [{'url': '/books/' + str(book.pk) + '/',
            'name': book.name} for book in books_filter]
  template = 'authors/author.pug'
  return render(request, template, {'author': author,
                                    'books': books})