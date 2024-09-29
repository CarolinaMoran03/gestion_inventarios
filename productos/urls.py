from django.urls import path
from . import views
from .views import login_view, logout_view, export_pdf, export_excel, export_pedidos_pdf, export_pedidos_excel, export_proveedores_pdf, export_proveedores_excel
from.views import login_redirect_view
urlpatterns = [
    path('', login_view, name='login'),  # Página de inicio de sesión como principal

    # URL para logout
    path('logout/', logout_view, name='logout'),
    path('base/', views.base, name='base'),
    path('login_redirect/', views.login_redirect_view, name='login_redirect'), 
    path('pedidos/', login_redirect_view, name='lista_pedidos'),
    path('proveedores/', login_redirect_view, name='lista_proveedores'),
    path('movimientos/', login_redirect_view, name='lista_movimientos'),

    # Rutas para exportar datos
    # productos
    path('export_pdf/', export_pdf, name='export_pdf'),
    path('export_excel/', export_excel, name='export_excel'),
    path('export_pedidos_pdf/', export_pedidos_pdf, name='export_pedidos_pdf'),
    path('export_pedidos_excel/', export_pedidos_excel, name='export_pedidos_excel'),
    path('export_proveedores_pdf/', export_proveedores_pdf, name='export_proveedores_pdf'),
    path('export_proveedores_excel/', export_proveedores_excel, name='export_proveedores_excel'),
    path('export_pdf_movimientos/', views.export_pdf_movimientos, name='export_pdf_movimientos'),
    path('export_excel_movimientos/', views.export_excel_movimientos, name='export_excel_movimientos'),

    # Página principal (podría mostrar un dashboard)
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),

    # Proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/<int:proveedor_id>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/<int:proveedor_id>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),

    # Pedidos
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/<int:pedido_id>/editar/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),

    # Movimientos
    path('movimientos/', views.lista_movimientos, name='lista_movimientos'),
    path('movimientos/<int:movimiento_id>/', views.detalle_movimiento, name='detalle_movimiento'),
    path('movimientos/nuevo/', views.crear_movimiento, name='crear_movimiento'),
    path('movimientos/<int:movimiento_id>/editar/', views.editar_movimiento, name='editar_movimiento'),
    path('movimientos/<int:movimiento_id>/eliminar/', views.eliminar_movimiento, name='eliminar_movimiento'),

    # Registro de usuarios
    path('registro/', views.registro, name='registro'), 
]
