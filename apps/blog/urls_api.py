from rest_framework.routers import DefaultRouter

from apps.blog.views_api import PostViewSet, CategoryViewSet, CommentViewSet

app_name = "blog"

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = router.urls
