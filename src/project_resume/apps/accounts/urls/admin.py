from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from project_resume.apps.accounts.views.admin import *

app_name = 'accounts_admin'



urlpatterns = [
    path('register',RegisterApiView.as_view(), name='register'),
    path('SendEmailPassword',SendEmailPassword.as_view(), name='forgot_password'),
    path('VerifyRestCode',VerifyRestCode.as_view(), name='VerifyRestCode'),
    path('newpassword',NewPassword().as_view(), name='new_password'),
]
