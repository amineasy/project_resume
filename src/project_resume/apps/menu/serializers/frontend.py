from django.db.models import Avg

from project_resume.apps.media.serializers.frontend import ImageSerializer
from project_resume.apps.menu.models import Dish, RatingDish, Menu, LikeDish
from rest_framework import serializers




class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name']

















class DishSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()
    class Meta:
        model = Dish
        fields = ['id','name','menu','price','discount_price','favorite','average_rating','is_liked','images']


    def get_average_rating(self,obj):
        avg = RatingDish.objects.filter(dish=obj).aggregate(avg=Avg('score'))['avg']
        return round(avg,1) if avg else 0

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            liked = LikeDish.objects.filter(dish=obj, user=user).exists()
            return liked
        return False

