from rest_framework import serializers
from .models import Books


class BookCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["title", "author", "publication_year", "created", "updated"]