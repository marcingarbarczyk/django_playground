from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()

urlpatterns = [
    path("blog/", include("apps.blog.urls_api")),
    path("books/", include("apps.books.urls_api")),
    path("shop/", include("apps.shop.urls_api")),
]
