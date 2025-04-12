from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project_resume.apps.menu.models import *
from project_resume.apps.menu.serializers.admin import RatingSerializer


class RatingDish(APIView):
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
