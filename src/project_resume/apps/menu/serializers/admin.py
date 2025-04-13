from rest_framework import serializers

from project_resume.apps.menu.models import RatingDish, LikeDish


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingDish
        fields = ['score','dish']






class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDish
        fields = '__all__'
