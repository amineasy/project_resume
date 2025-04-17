from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project_resume.apps.cart.session.session import Cart
from project_resume.apps.menu.models import Dish
from project_resume.apps.menu.serializers.frontend import DishSerializer




class AddCart(APIView):
    permission_classes = (AllowAny,)
    def post(self, request,dish_id):
        cart = Cart(request)
        try:
            dish = Dish.objects.get(id=dish_id)
            cart.add_cart(dish)
            return Response({'message':'با موفقیت اضافه شد'},status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'error':'غذا پیدا نشد'},status=status.HTTP_400_BAD_REQUEST)







class RemoveAllFromCartView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, dish_id):
        cart = Cart(request)
        try:
            dish = Dish.objects.get(id=dish_id)
            cart.remove_all(dish)
            return Response({"message":'با موفقیت حذف شد'},status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'error':'غذا پیدا نشد'},status=status.HTTP_400_BAD_REQUEST)



class RemoveSingleCartView(APIView):
    def delete(self, request, dish_id):
        cart = Cart(request)
        try:
            dish = Dish.objects.get(id=dish_id)
            cart.remove_single(dish)
            return Response({'message':'با موفقیت حذف شد'},status=status.HTTP_200_OK)
        except Dish.DoesNotExist:
            return Response({'error':'غذا پیدا نشد'},status=status.HTTP_400_BAD_REQUEST)




