from django.urls import path
from .views import *

urlpatterns = [
    path('books/', get_books),
    path('book/<int:id>/', get_book),
    path('authors/', get_authors),
    path('author/<int:id>/', get_author),
    path('author/<int:id>/books/', get_author_books),
]