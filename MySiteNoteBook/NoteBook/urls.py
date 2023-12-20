from django.urls import path
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_swagger.views import get_swagger_view

shema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path('', NoteListView.as_view(), name='home'),
    path('tnx/', tnx, name='tnx'),
path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
