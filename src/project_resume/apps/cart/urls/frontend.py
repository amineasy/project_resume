from django.urls import path

from project_resume.apps.cart.views.frontend import CartDetailAPIView, CartTotalPriceAPIView

app_name = 'cart_frontend'




urlpatterns = [
    path('cart/',CartDetailAPIView.as_view(),name='cart_detail'),
    path('total_price_cart/',CartTotalPriceAPIView.as_view(),name='cart_total_price'),

]