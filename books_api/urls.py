from django.conf.urls import url
from django.urls import path, include
from .views import (
    BooksCollectionApiView,
    BooksCollectionDetailApiView
)

urlpatterns = [
    path('api', BooksCollectionApiView.as_view()),
    path('api/<int:book_id>/', BooksCollectionDetailApiView.as_view()),
]