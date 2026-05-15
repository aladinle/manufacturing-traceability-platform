from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ComponentViewSet, ProductViewSet, AssemblyViewSet, AuditLogViewSet
    , product_traceability)

router = DefaultRouter()
router.register("components", ComponentViewSet, basename='component')
router.register("products", ProductViewSet, basename='product')
router.register("assemblies", AssemblyViewSet, basename='assembly')
router.register("audit-logs", AuditLogViewSet, basename='auditlog')

urlpatterns = [
    path('', include(router.urls)),
    path("traceability/<str:serial_number>/", product_traceability),
]