

from django.contrib import admin

from project_resume.apps.media.models import DishImage, BranchImage, MenuImage


class DishImageInline(admin.TabularInline):
    model = DishImage
    extra = 1
    fields = ['image']




class BranchImageInline(admin.TabularInline):
    model = BranchImage
    extra = 1
    fields = ['branch', 'image']





class MenuImageInline(admin.TabularInline):
    model = MenuImage
    extra = 1
    fields = ['menu', 'image']









admin.site.register(DishImage)
admin.site.register(BranchImage)
admin.site.register(MenuImage)