from django.contrib import admin
from .models import Producto, Proveedor, Pedido, MovimientoInventario

# Registrar los modelos
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(MovimientoInventario)
