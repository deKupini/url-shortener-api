from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import URLMappingViewSet

router = DefaultRouter()
router.register(r"", URLMappingViewSet, basename="shortened-url")

urlpatterns = [
    path("", include(router.urls)),
]