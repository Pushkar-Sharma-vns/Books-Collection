from django.test import TestCase
from .factory import BooksFactory
from ..serializers import BookCollectionSerializer


class BookCollectionSerializerTestCase(TestCase):
    def test_book_collection_serializer(self):
        book = BooksFactory()
        serializer = BookCollectionSerializer(book)
        
        self.assertEqual(serializer.data["title"], book.title)
        self.assertEqual(serializer.data["author"], book.author)