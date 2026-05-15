from django.contrib import admin
from .models import Component, Product, Assembly, AuditLog

# Register your models here.
admin.site.register(Component)
admin.site.register(Product)
admin.site.register(Assembly)
admin.site.register(AuditLog)
