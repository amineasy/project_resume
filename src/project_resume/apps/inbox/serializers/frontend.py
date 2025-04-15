from rest_framework import serializers

from project_resume.apps.inbox.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name','address','phone','working_days']
