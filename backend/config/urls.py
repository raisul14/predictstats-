from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Swagger API Documentation Setup
schema_view = get_schema_view(
    openapi.Info(
        title="PredictStats API",
        default_version='v1',
        description="AI Football Prediction Platform API",
        terms_of_service="https://predictstats.com/terms/",
        contact=openapi.Contact(email="api@predictstats.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin Panel (Secure Path)
    path(
        f"{settings.ADMIN_URL}/", 
        admin.site.urls
    ),
    
    # API Endpoints
    path('api/v1/', include([
        path('', include('core.urls')),  # Core app endpoints
        path('predictions/', include('prediction_engine.urls')),  # AI prediction endpoints
        path('data/', include('data_pipeline.urls')),  # Data pipeline endpoints
    ])),
    
    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Development-only URLs
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]  # Profiling

# Error Handlers
handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'
