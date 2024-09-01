from django.db import models
from django.db.models import F
class Proveedor(models.Model):
    codigo = models.CharField(max_length=10, unique=True, editable=False)  # No editable
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.codigo:
            # Generar un código único para el proveedor si no se ha proporcionado
            last_proveedor = Proveedor.objects.order_by('-id').first()
            if last_proveedor:
                self.codigo = str(int(last_proveedor.codigo) + 1)
            else:
                self.codigo = '001'  # Valor inicial o lógico de inicio
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.codigo:  # Genera el código solo si no está presente
            last_producto = Producto.objects.all().order_by('-id').first()
            if last_producto and last_producto.codigo:
                last_codigo = last_producto.codigo
                next_codigo = str(int(last_codigo) + 1).zfill(3)
            else:
                next_codigo = '001'
            self.codigo = next_codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} ({self.codigo})'

    @property
    def estado_stock(self):
        try:
            stock = int(self.stock_actual)
        except ValueError:
            stock = 0
        return 'Agotado' if stock <= 0 else f'{stock} en stock'

class Pedido(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    fecha_pedido = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')])

    def save(self, *args, **kwargs):
        if not self.codigo:  # Genera el código solo si no está presente
            last_pedido = Pedido.objects.all().order_by('-id').first()
            if last_pedido and last_pedido.codigo:
                last_codigo = last_pedido.codigo
                next_codigo = str(int(last_codigo) + 1).zfill(3)
            else:
                next_codigo = '001'
            self.codigo = next_codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Pedido {self.codigo} - {self.proveedor.nombre}'

class MovimientoInventario(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=50, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    cantidad = models.IntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    lote = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Actualizar el código del movimiento si no está presente
        if not self.codigo:
            last_movimiento = MovimientoInventario.objects.all().order_by('-id').first()
            if last_movimiento and last_movimiento.codigo:
                last_codigo = last_movimiento.codigo
                next_codigo = str(int(last_codigo) + 1).zfill(3)
            else:
                next_codigo = '001'
            self.codigo = next_codigo

        # Actualizar el stock del producto basado en el tipo de movimiento
        if self.tipo_movimiento == 'entrada':
            self.producto.stock_actual = F('stock_actual') + self.cantidad
        elif self.tipo_movimiento == 'salida':
            self.producto.stock_actual = F('stock_actual') - self.cantidad
        
        self.producto.save()  # Guardar la actualización en el producto

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.codigo} - {self.tipo_movimiento} - {self.producto.codigo} - {self.cantidad}'