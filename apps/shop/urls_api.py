from rest_framework.routers import DefaultRouter

from apps.shop.views_api import (
    ProductViewSet,
    CategoryViewSet,
    ProductVoteViewSet,
    OrderItemViewSet,
    OrderViewSet,
    DeliveryAddressViewSet,
    CartItemViewSet,
    CartViewSet,
)

app_name = "shop"

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"product_votes", ProductVoteViewSet)
router.register(r"order", OrderViewSet)
router.register(r"order_items", OrderItemViewSet)
router.register(r"cart", CartViewSet)
router.register(r"cart_items", CartItemViewSet)
router.register(r"delivery_addresses", DeliveryAddressViewSet)

urlpatterns = router.urls
