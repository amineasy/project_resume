from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from project_resume.apps.inbox.models import Branch
from project_resume.apps.inbox.serializers.frontend import BranchSerializer


class BranchApiView(APIView):
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)




class BranchDetailApiView(APIView):

    def get(self, request, id):
        branch = get_object_or_404(Branch,id=id)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
