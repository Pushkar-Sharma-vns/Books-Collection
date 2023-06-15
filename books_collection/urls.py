from django.contrib import admin
from django.urls import path, include
from books_api import urls as book_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('books/', include(book_urls)),
]
