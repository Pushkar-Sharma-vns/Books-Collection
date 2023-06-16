from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..views import BooksCollectionApiView, BooksCollectionDetailApiView
from ..models import Books
from ..serializers import BookCollectionSerializer
from .factory import BooksFactory


class BooksCollectionApiViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_books_collection(self):
        BooksFactory.create_batch(3)
        request = self.factory.get('/books/api')
        view = BooksCollectionApiView.as_view()

        response = view(request)
        books = Books.objects.all()
        serializer = BookCollectionSerializer(books, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create_book_record(self):
        book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': '2023-01-01T00:00:00Z',
        }
        request = self.factory.post('/books/api', book_data)
        view = BooksCollectionApiView.as_view()

        response = view(request)
        book = Books.objects.last()
        serializer = BookCollectionSerializer(book)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)


class BooksCollectionDetailApiViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.book = BooksFactory()

    def test_get_book_record(self):
        request = self.factory.get('/books/api/1/')
        view = BooksCollectionDetailApiView.as_view()

        response = view(request, book_id=self.book.id)
        serializer = BookCollectionSerializer(self.book)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_update_book_record(self):
        updated_data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': '2022-01-01 00:00:00+00:00',
        }
        request = self.factory.put('/books/api/1/', updated_data)
        view = BooksCollectionDetailApiView.as_view()

        response = view(request, book_id=self.book.id)
        self.book.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.book.title, updated_data['title'])
        self.assertEqual(self.book.author, updated_data['author'])
        self.assertEqual(str(self.book.publication_year), updated_data['publication_year'])

    def test_delete_book_record(self):
        request = self.factory.delete('/books/api/1/')
        view = BooksCollectionDetailApiView.as_view()

        response = view(request, book_id=self.book.id)
        exists = Books.objects.filter(id=self.book.id).exists()

        self.assertEqual(response.status_code, 204)
        self.assertFalse(exists)