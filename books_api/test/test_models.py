from django.test import TestCase

from ..models import Books
from .factory import BooksFactory


class BookTestCase(TestCase):
    book = BooksFactory()
    
    def test_book_str_method(self):
        '''Testing for str representation'''
        self.assertEqual(str(self.book), self.book.title)
        
    def test_book_creation(self):
        self.assertIsInstance(self.book, Books)
        self.assertIsNotNone(self.book.id)
        self.assertIsNotNone(self.book.title)
        self.assertIsNotNone(self.book.author)
        self.assertIsNotNone(self.book.publication_year)
        self.assertIsNotNone(self.book.created)
        self.assertIsNotNone(self.book.updated)