from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ClientViewSet, HealthProgramViewSet, client_detail, AppointmentListCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'programs', HealthProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),  # <-- This already handles /clients/ and /programs/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('appointments/', AppointmentListCreate.as_view(), name='appointment-list-create'),  # <-- Add your appointments separately
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
