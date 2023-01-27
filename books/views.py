from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    """A view for the Book model"""
    model = Book
    template_name = 'book_list.html'
