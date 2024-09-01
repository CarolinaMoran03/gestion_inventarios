from django import forms
from .models import Proveedor, Producto, Pedido, MovimientoInventario

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'}),
            'telefono': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'}),
            'direccion': forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50', 'rows': 3}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['codigo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50', 'rows': 3}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['codigo']  # Excluye el campo 'codigo' del formulario
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'type': 'date'}),
            'proveedor': forms.Select(),
            'productos': forms.CheckboxSelectMultiple(),
            'estado': forms.Select(choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')]),
        }

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        exclude = ['codigo']  # Excluye el campo 'codigo' del formulario
        widgets = {
            'lote': forms.TextInput(attrs={'placeholder': 'Número de lote (opcional)'}),
        }
