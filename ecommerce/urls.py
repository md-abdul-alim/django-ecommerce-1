from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    CheckoutView,
    add_to_cart,
    remove_to_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)
#from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('accounts/profile/',HomeView.as_view(),name='profile'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_to_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/',PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/',RequestRefundView.as_view(), name='request-refund')
]
