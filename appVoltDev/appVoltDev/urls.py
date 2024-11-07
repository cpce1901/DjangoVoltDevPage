from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', include('apps.core.urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += path("admin/", admin.site.urls),
    urlpatterns += path('schema/', SpectacularAPIView.as_view(), name='schema'),
    urlpatterns += path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
