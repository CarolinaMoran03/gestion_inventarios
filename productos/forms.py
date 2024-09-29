from django import forms
from .models import Proveedor, Producto, Pedido, MovimientoInventario

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'placeholder': 'Nombre del proveedor'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'placeholder': 'Teléfono del proveedor'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'rows': 3,
                'placeholder': 'Dirección del proveedor'
            }),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['codigo']  # Excluye el campo 'codigo' del formulario
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'rows': 3,
                'placeholder': 'Descripción del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'placeholder': 'Precio del producto'
            }),
            'stock_actual': forms.NumberInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
                'placeholder': 'Stock actual'
            }),
            'ubicacion': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            }),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['codigo']  # Excluye el campo 'codigo' del formulario
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            }),
            'productos': forms.CheckboxSelectMultiple(attrs={
                'class': 'mt-1',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            }),
        }

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        exclude = ['codigo']  # Excluye el campo 'codigo' del formulario
        widgets = {
            'lote': forms.TextInput(attrs={
                'placeholder': 'Número de lote (opcional)',
                'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            }),
        }
