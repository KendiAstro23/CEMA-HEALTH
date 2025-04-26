from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ClientViewSet, HealthProgramViewSet, client_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'programs', HealthProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/clients/<int:pk>/', client_detail, name='client-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
