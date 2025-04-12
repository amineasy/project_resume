from rest_framework import serializers

from project_resume.apps.menu.models import RatingDish


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingDish
        fields = ['score','dish']


