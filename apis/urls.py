from django.urls import path

from .views import BookAPIView

app_name = 'apis'
urlpatterns = [
    # URL for Book web API
    path('', BookAPIView.as_view(), name='book_api'),
]