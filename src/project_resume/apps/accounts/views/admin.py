from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project_resume.apps.accounts.serializers.admin import *


class RegisterApiView(APIView):


    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

