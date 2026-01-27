from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi

# Import your API views
from google.views import location_list_create_api_view, location_retrieve_update_delete_api_view

# Create schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Your existing API URLs
    path('api/locations/', location_list_create_api_view, name='location-list-create'),
    path('api/locations/<int:pk>/', location_retrieve_update_delete_api_view, name='location-retrieve-update-delete'),

    # Swagger documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Schema JSON URL
    path('swagger/api.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]