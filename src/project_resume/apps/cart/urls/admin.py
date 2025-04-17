from django.urls import path

from project_resume.apps.cart.views.admin import AddCart, RemoveAllFromCartView, RemoveSingleCartView

app_name = 'cart_admin'
urlpatterns = [
    path('addcart/<int:dish_id>/',AddCart.as_view(),name='add_cart'),
    path('remove-cart/<int:dish_id>/',RemoveAllFromCartView.as_view(),name='remove_all_cart'),
    path('remove-single-cart/<int:dish_id>/',RemoveSingleCartView.as_view(),name='remove_all_cart'),



]
