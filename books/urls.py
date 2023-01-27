from django.urls import path

from .views import BookListView

app_name = 'books'
urlpatterns = [
    # Home page url
    path('', BookListView.as_view(), name='book_list'),
]