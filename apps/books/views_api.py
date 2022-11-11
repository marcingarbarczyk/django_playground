from rest_framework.viewsets import ModelViewSet

from apps.books.models import Book, Author, Store, Publisher
from apps.books.serializers import (
    BookSerializer,
    StoreSerializer,
    AuthorSerializer,
    PublisherSerializer,
)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
