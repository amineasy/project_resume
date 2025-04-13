from django.contrib import admin

from project_resume.apps.media.admin import DishImageInline
from project_resume.apps.menu.models import Menu, Dish, LikeDish


class DishAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [DishImageInline]








admin.site.register(Dish,DishAdmin)
admin.site.register(Menu)
admin.site.register(LikeDish)