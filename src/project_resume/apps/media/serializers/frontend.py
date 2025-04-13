from rest_framework import serializers

from project_resume.apps.media.models import DishImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = ['id', 'image']