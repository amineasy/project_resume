

from django.contrib import admin

from project_resume.apps.media.models import DishImage







class DishImageInline(admin.TabularInline):
    model = DishImage
    extra = 1
    fields = ['name', 'image']





admin.site.register(DishImage)