from django.urls import path

from project_resume.apps.menu.views.admin import RatingDish

app_name = 'menu_admin'




urlpatterns = [
    path('rating-dish',RatingDish.as_view(), name='rating_dish'),
]


