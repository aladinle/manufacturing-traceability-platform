from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Component, Product, Assembly, AuditLog
from .serializers import (
    ComponentSerializer, ProductSerializer, AssemblySerializer, AuditLogSerializer
)

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class AssemblyViewSet(viewsets.ModelViewSet):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer
    permission_classes = [IsAuthenticated]

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_traceability(request, serial_number):
    """
    API endpoint to retrieve the traceability information for a product.
    """
    try:
        product = Product.objects.get(serial_number=serial_number)
        assemblies = Assembly.objects.filter(product=product)
        component_data = []

        for assembly in assemblies:
            component_data.append({"component_serial": assembly.component.serial_number,
                "part_number": assembly.component.part_number,
                "component_type": assembly.component.component_type,
                "installed_at": assembly.installed_at,
                "station_id": assembly.station_id,
            })


        return Response({
            "product_serial": product.serial_number,
            "product_model": product.product_model,
            "components": component_data,
            "status": product.status,
        })

    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)