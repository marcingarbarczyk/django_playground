from django.contrib import admin

from apps.shop.models import (
    Product,
    Order,
    OrderItem,
    Category,
    DeliveryAddress,
    ProductVote,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("title",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "city",
        "state",
        "zip_code",
        "total",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    search_fields = ("order", "product")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "state", "zip_code", "user")
    search_fields = ("address", "city", "state", "zip_code")


@admin.register(ProductVote)
class ProductVoteAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "vote",
        "user",
    )
    search_fields = (
        "product",
        "vote",
        "user",
    )
