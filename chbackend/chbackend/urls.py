from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api.views import ClientViewSet, HealthProgramViewSet, AppointmentListCreate, AppointmentViewSet, PublicClientProfileView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'programs', HealthProgramViewSet, basename='program')
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),  # <-- This already handles /clients/ and /programs/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('appointments/', AppointmentListCreate.as_view(), name='appointment-list-create'),  # Add appointments
    path('public/clients/<int:pk>/', PublicClientProfileView.as_view(), name='public-client-profile'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
