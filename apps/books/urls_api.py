from rest_framework.routers import DefaultRouter

from apps.books.views_api import (
    BookViewSet,
    StoreViewSet,
    AuthorViewSet,
    PublisherViewSet,
)

app_name = "books"

router = DefaultRouter()
router.register(r"book", BookViewSet)
router.register(r"publisher", PublisherViewSet)
router.register(r"author", AuthorViewSet)
router.register(r"store", StoreViewSet)

urlpatterns = router.urls
