from django.conf.urls import url
from django.urls import path, include
from .views import (
    BooksCollectionApiView
)

urlpatterns = [
    path('api', BooksCollectionApiView.as_view()),
]