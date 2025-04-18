from django.contrib import admin

from project_resume.apps.inbox.models import *
from project_resume.apps.media.admin import BranchImageInline


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (BranchImageInline,)







admin.site.register(FeedBack)
admin.site.register(Branch,BranchAdmin)
