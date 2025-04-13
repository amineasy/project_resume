from django.urls import path

from project_resume.apps.menu.views.admin import RateDishView,LikeCreate

app_name = 'menu_admin'




urlpatterns = [
    path('rating-dish',RateDishView.as_view(), name='rating_dish'),
    path('likecreate/<int:dish_id>',LikeCreate.as_view(), name='likecreate'),
]


