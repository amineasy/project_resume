from django.urls import path
from project_resume.apps.inbox.views.frontend import BranchApiView, BranchDetailApiView, SearchAPIView

app_name = 'inbox_frontend'

urlpatterns = [
    path('branchs/', BranchApiView.as_view(), name='branch'),
    path('branchs/<int:id>/', BranchDetailApiView.as_view(), name='branch-detail'),
    path('search/',SearchAPIView.as_view(), name='search'),
]
