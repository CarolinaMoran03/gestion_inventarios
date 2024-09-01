from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto, Proveedor, Pedido, MovimientoInventario

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(MovimientoInventario)

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Producto  # Modelo para ejemplo

# Crear grupo
admin_group, created = Group.objects.get_or_create(name='Administrador')

# Asignar permisos
content_type = ContentType.objects.get_for_model(Producto)
permisos = Permission.objects.filter(content_type=content_type)
admin_group.permissions.set(permisos)  # Asignar todos los permisos de Producto al grupo Admin
