from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project_resume.apps.menu.models import Menu, Dish, LikeDish
from project_resume.apps.menu.serializers.frontend import DishSerializer


class DishesByMainMenuView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, main_menu_id):
        try:
            main_menu = Menu.objects.get(id=main_menu_id, parent__isnull=True)
        except Menu.DoesNotExist:
            return Response({"error": "منو پیدا نشد"}, status=404)

        sub_menus = Menu.objects.filter(parent=main_menu).prefetch_related('dishes')

        submenu_data = []
        for sub in sub_menus:

            dish_serializer = DishSerializer(sub.dishes.all(), many=True,context={'request': request})
            submenu_data.append({
                "submenu_name": sub.name,
                "submenu_id": sub.id,
                "dishes": dish_serializer.data
            })

        return Response({
            "main_menu": main_menu.name,
            "sub_menu": submenu_data
        })








class FavouriteDishes(APIView):
    Permission_classes = (IsAuthenticated,)


    def get(self, request):
        liked_dishes = LikeDish.objects.filter(user=request.user)

        dish_ids = liked_dishes.values_list('dish_id', flat=True)

        dishes = Dish.objects.filter(id__in=dish_ids)

        serializer = DishSerializer(dishes, many=True)

        return Response(serializer.data)


