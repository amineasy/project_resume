from django.urls import path

from project_resume.apps.menu.views.frontend import *

app_name = 'menu_frontend'



urlpatterns = [
    path('menu/<int:main_menu_id>/dishes/', DishesByMainMenuView.as_view(), name='dish_list'),
]