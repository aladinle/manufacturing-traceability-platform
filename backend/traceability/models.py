from django.db import models
from django.contrib.auth.models import User

class Component(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    part_number = models.CharField(max_length=100)
    component_type = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, default="RECEIVED")
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    product_model = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="CREATED")
    created_at = models.DateTimeField(auto_now_add=True)

class Assembly(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    installed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    station_id = models.CharField(max_length=100)
    installed_at = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=100)
    entity_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
