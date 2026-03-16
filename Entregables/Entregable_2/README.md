# Análisis de ventas — reproducibilidad

Este repositorio contiene cuadernos y scripts para el análisis de ventas (EDA): identificación de producto más vendido, consumo por ciudad y análisis estadístico básico.

Ubicación principal de outputs:
- `analysis_outputs/` — gráficos PNG y CSVs generados por los scripts/notebooks.
- Notebooks principales:
  - `analysis.ipynb` — notebook de análisis (creado pero la ejecución automática tuvo problemas de encoding en rutas con caracteres especiales).
  - `analysis_executed.ipynb` — versión con células que cargan y muestran los resultados generados.

Requisitos (Python)
- Se recomienda usar Python 3.11+ o 3.12 en un entorno virtual.
- Instalar dependencias listadas en `requirements.txt`.

Pasos para reproducir (Windows PowerShell)
1. Crear y activar un entorno virtual (PowerShell):

```powershell
python -m venv .venv
# activar en PowerShell
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. (Recomendado) Forzar UTF-8 en la salida de Python para evitar errores de codificación en consolas Windows con rutas que contienen caracteres no-ASCII:

```powershell
# en la sesión actual
$env:PYTHONUTF8 = "1"
# o para persistir en el sistema (requiere reinicio de sesión)
setx PYTHONUTF8 1
```

Nota sobre rutas con emoji o caracteres no-ASCII
- En varias ejecuciones automáticas observamos errores de codificación cuando la ruta del proyecto contiene emoji o caracteres especiales. Si ves errores como `UnicodeEncodeError` al ejecutar notebooks o pip, renombrar la carpeta de trabajo a una ruta sin caracteres especiales (por ejemplo `C:\Users\HP0340\Desktop\curso\BASE_DE_DATOS`) evita la mayoría de problemas.

Archivos y comandos útiles
- Convertir todos los `.xlsx` a `.csv` (ya se proporcionó y ejecutó en este proyecto):

```powershell
# Ejecutar el script de conversión
.\.venv\Scripts\python.exe convert_xlsx_to_csv.py
```

- Abrir el notebook con Jupyter (lanzará el navegador):

```powershell
.\.venv\Scripts\python.exe -m jupyter lab
# o
.\.venv\Scripts\python.exe -m jupyter notebook
```

Outputs principales generados en `analysis_outputs/` (ejemplos)
- `top_products_qty.png`, `top_products_sales_normalized.png`
- `top_cities_by_importe.png`, `city_aggregation_by_importe.csv`
- `correlations_pairs_scipy.csv`, `correlation_heatmap_scipy.png`, `city_metrics_scipy.csv`
- `analysis_stats_scipy.txt` (resumen estadístico)

Qué más se puede hacer
- Ejecutar `analysis_executed.ipynb` en Jupyter para ver las figuras inline.
- Revisar y limpiar manualmente `Detalle_ventas.csv` para eliminar columnas `Unnamed:*` y confirmar unidades monetarias.
- Añadir `requirements.txt` con versiones fijas si deseas reproducibilidad estricta (p. ej. `pandas==2.2.3`).

Contacto
- Si quieres que automatice más pasos (RFM, top-20 productos por importe, exportar un informe PDF), dime cuál y lo añado al notebook.
