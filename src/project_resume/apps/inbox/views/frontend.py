from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from project_resume.apps.inbox.models import Branch
from project_resume.apps.inbox.serializers.frontend import BranchSerializer
from project_resume.apps.menu.models import Dish
from project_resume.apps.menu.serializers.frontend import DishSerializer


class BranchApiView(APIView):
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)


class BranchDetailApiView(APIView):

    def get(self, request, id):
        branch = get_object_or_404(Branch, id=id)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)




class SearchAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        query = request.query_params.get('q', None)

        if not query:
            return Response({"message": "لطفاً عبارت جستجو را وارد کنید."}, status=status.HTTP_400_BAD_REQUEST)

        dishes = Dish.objects.filter(name__icontains=query)

        serializer = DishSerializer(dishes, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

