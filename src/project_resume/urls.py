from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static

admin_urls = [
    path('backend/api/', include('project_resume.apps.accounts.urls.admin', namespace='accounts_admin')),
    path('backend/api/', include('project_resume.apps.menu.urls.admin', namespace='menu_admin')),
    path('backend/login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




drf_spectacular = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]




urlpatterns = [
    path('admin/', admin.site.urls),
] + admin_urls + drf_spectacular



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
