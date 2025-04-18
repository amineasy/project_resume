from urllib import request

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project_resume.apps.cart.session.session import Cart
from project_resume.apps.menu.models import Dish
from project_resume.apps.menu.serializers.frontend import DishSerializer


class CartDetailAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        cart = Cart(request)
        data = []
        total_price_cart = 0#برای مقدار دهی اولیه

        for item in cart:
            price_after_discount = item['dish'].get_total_price()
            total_price_by_quantity = price_after_discount * item['quantity']
            total_price_cart += total_price_by_quantity

            data.append({
                'dish': DishSerializer(item['dish'], context={'request': request}).data,
                'price_after_discount': price_after_discount,
                'quantity': item['quantity'],
                'total_price_by_quantity': total_price_by_quantity
            })


        return Response({
            'data': data,
            'total_price_all_item': total_price_cart,
            'total_discount_all_item': cart.get_total_discount()
        })






class CartTotalPriceAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        cart = Cart(request)
        total_price = cart.get_total_price()
        return Response({'total_price':total_price})

