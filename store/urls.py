from django.urls import path
from .views import ShopView, CartView, ProductSingleView, CartViewSet, WishlistView,\
    WishlistViewSet, wishlist_add, wishlist_delete
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'wishlist', WishlistViewSet)

app_name = 'store'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/add/<int:id>/', wishlist_add, name='add_to_wishlist'),
    path('wishlist/delete/<int:id>/', wishlist_delete, name='delete_from_wishlist'),
]
