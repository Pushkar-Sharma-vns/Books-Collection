import factory
from ..models import Books
from datetime import datetime


class BooksFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Books

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')
    publication_year = factory.LazyFunction(datetime.now)