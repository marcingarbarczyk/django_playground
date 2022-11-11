from rest_framework.serializers import ModelSerializer

from apps.books.models import Author, Store, Publisher, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
