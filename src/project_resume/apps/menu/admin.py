from django.contrib import admin

from project_resume.apps.media.admin import DishImageInline, MenuImageInline
from project_resume.apps.menu.models import Menu, Dish, LikeDish


class DishAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [DishImageInline]



class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [MenuImageInline]






admin.site.register(Dish,DishAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(LikeDish)