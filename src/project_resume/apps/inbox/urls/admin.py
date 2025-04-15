from django.urls import path
from project_resume.apps.inbox.views.admin import FeedBackCreatedAPIView

app_name = 'inbox_admin'



urlpatterns = [
    path('feedback',FeedBackCreatedAPIView.as_view(),name='feedback'),
]