# productos/management/commands/generate_reports.py
from django.core.management.base import BaseCommand
from productos.models import Producto
import pandas as pd
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Genera reportes automáticos de productos'

    def handle(self, *args, **kwargs):
        # Filtra productos con bajo stock (puedes ajustar el límite)
        low_stock_products = Producto.objects.filter(stock_actual__lt=10)  
        
        # Crea un DataFrame de los productos
        df = pd.DataFrame(list(low_stock_products.values()))

        # Define la ruta de salida para el reporte
        report_dir = 'reportes'
        os.makedirs(report_dir, exist_ok=True)  # Crea el directorio si no existe
        
        # Genera el nombre del archivo de reporte
        report_filename = os.path.join(report_dir, f'bajo_stock_{timezone.now().strftime("%Y%m%d")}.xlsx')

        # Guarda el DataFrame en un archivo Excel
        df.to_excel(report_filename, index=False)
        self.stdout.write(self.style.SUCCESS(f'Reporte de bajo stock generado: {report_filename}'))
