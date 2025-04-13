from django.urls import path

from project_resume.apps.menu.views.admin import RateDishView

app_name = 'menu_admin'




urlpatterns = [
    path('rating-dish',RateDishView.as_view(), name='rating_dish'),
]


