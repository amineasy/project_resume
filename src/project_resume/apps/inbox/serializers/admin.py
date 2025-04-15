from rest_framework import serializers

from project_resume.apps.inbox.models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = ['id', 'fullname', 'phone_number', 'email', 'message']

