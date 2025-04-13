from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project_resume.apps.menu.models import *
from project_resume.apps.menu.serializers.admin import RatingSerializer


class RateDishView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            score = serializer.validated_data['score']
            dish = serializer.validated_data['dish']
            user = request.user

            rating, created = RatingDish.objects.update_or_create(
                user=user, dish=dish, defaults={'score': score}
            )

            return Response({
                "message": "با موفقیت امتیاز ثبت شد.",
                "new": created,
                "score": score
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, dish_id):
        try:
            dish = Dish.objects.get(id=dish_id)
        except Dish.DoesNotExist:
            return Response({"message": "غذا پیدا نشد."}, status=status.HTTP_404_NOT_FOUND)

        if LikeDish.objects.filter(user=request.user, dish=dish).exists():
            LikeDish.objects.filter(user=request.user, dish=dish).delete()
            return Response({'message': 'لایک حذف شد'}, status=status.HTTP_200_OK)

        LikeDish.objects.create(user=request.user, dish=dish)
        return Response({"message": "لایک با موفقیت ثبت شد. برای دیدن به لیست علاقه‌مندی‌ها مراجعه کنید."}, status=status.HTTP_201_CREATED)




