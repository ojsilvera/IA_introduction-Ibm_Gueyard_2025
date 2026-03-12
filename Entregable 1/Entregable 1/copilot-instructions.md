<!-- copilot-instrucciones.md - Guía para agentes de IA que colaboran en este repositorio -->

# Instrucciones para Copilot / agente de IA en "EnriqueParada-Proyecto_Aurelion"

Este proyecto es una demostración pequeña de análisis de datos centrada en limpiar y analizar cuatro archivos CSV (`clientes`, `ventas`, `detalle_ventas`, `productos`). El script principal ejecutable es `programa.py` y la documentación está en `DOCUMENTACION.md`.

Mantén las instrucciones breves, prácticas y específicas para los archivos de este repositorio.

## Datos clave (útiles para sugerencias de código)
- **Propósito**: corregir inconsistencias en los datos (especialmente valores de `categoria` en `productos.csv`), normalizar tablas, calcular RFM y crear reportes o visualizaciones simples.
- **Script principal**: `programa.py` — una interfaz de línea de comandos con menú textual que imprime documentación y sugerencias. Cualquier cambio debe preservar el comportamiento del menú, salvo que se convierta a otra interfaz.
- **Fuente de verdad para el esquema de datos y problemas**: `DOCUMENTACION.md` (contiene tipos de columnas, ejemplos de productos mal clasificados y pasos recomendados).

## Estructura del proyecto para referencia en sugerencias
- `programa.py` — CLI y punto de entrada principal. Usa este archivo para agregar demostraciones, funciones pequeñas de procesamiento o ejemplos de lectura de CSV.
- `DOCUMENTACION.md` — descripción detallada del conjunto de datos y reglas de limpieza requeridas (reclasificar categorías, eliminar columnas redundantes).

## Convenciones y patrones detectados
- Mantén el código mínimo y sin dependencias pesadas para fines demostrativos. Evita agregar frameworks grandes salvo que se solicite explícitamente.
- Usa solo la biblioteca estándar de Python 3.x. Si sugieres nuevas dependencias, justifícalas y proporciona un `requirements.txt` mínimo y un snippet corto de instalación.
- Conserva el idioma español en la salida del CLI. Si agregas texto nuevo para el usuario, mantén la coherencia en español.

## Tareas sugeridas para colaboradores
- Agregar una utilidad pequeña para cargar CSV (usando `csv` de la biblioteca estándar o `pandas` si se solicita) que demuestre cómo unir `detalle_ventas` + `productos` para calcular ingresos por producto.
- Implementar una función de reclasificación categórica usando un diccionario basado en reglas para corregir `categoria` en `productos.csv`. Usa ejemplos de `DOCUMENTACION.md`.
- Agregar una opción `--demo` o del menú que ejecute un pequeño pipeline de extremo a extremo (cargar CSVs, corregir categorías, calcular los 5 productos con más ingresos) y que imprima una tabla corta.
- Agregar pruebas unitarias ligeras para funciones de limpieza deterministas (por ejemplo, `reclassify_category(name: str) -> str`).

## Qué NO hacer
- No asumas que existen carpetas adicionales, sistemas de construcción o configuraciones de CI. Este repositorio no tiene pruebas, archivos de configuración ni workflows en `.github`.
- No refactorices el proyecto como una aplicación grande sin confirmar el alcance. Mantén los cambios pequeños y reversibles.

## Ejemplos del código base para referencia
- El bucle del menú en `programa.py` (preservar comportamiento):
  - Basado en entrada: `mostrar_menu()` devuelve una opción como cadena y `main()` usa `while True` + if/elif para despachar.
  - Las instrucciones `print` y los mensajes en español son la superficie visible para el usuario. Mantenlos intactos por defecto.
- `DOCUMENTACION.md` lista ejemplos mal clasificados (por ejemplo, `Pepsi`, `Shampoo`) — úsalos como datos iniciales al implementar heurísticas de reclasificación.

## Flujos de trabajo recomendados para desarrolladores
- Ejecuta el script localmente con Python del sistema: `python programa.py` (en PowerShell de Windows: `python .\programa.py`).
- Si agregas dependencias, proporciona `requirements.txt` y recomienda:
  - `python -m venv .venv`
  - `.venv\Scripts\Activate.ps1`
  - `pip install -r requirements.txt`

## Casos especiales y restricciones observadas
- Los ejemplos del conjunto de datos son pequeños; evita optimizaciones pesadas. Prioriza claridad y reproducibilidad.
- Cualquier código de lectura de CSV debe tolerar columnas redundantes (por ejemplo, `nombre_cliente`, `email`) y preferir uniones por claves `id_` como se documenta.

## Si modificas archivos, sigue estas reglas
- Mantén los cambios pequeños (una función o corrección por PR). Incluye un comentario corto en español describiendo el cambio.
- Agrega pruebas unitarias para lógica determinista. Para flujos de I/O o demostración, proporciona una opción `--dry-run` o `--demo` que no requiera red ni servicios externos.

## Consulta al usuario antes de:
- Introducir servicios de terceros o frameworks pesados (Dash, Streamlit, bases de datos).
- Cambiar el idioma visible para el usuario de español a otro idioma.

## Retroalimentación
- Después de aplicar cambios, pide al revisor humano que confirme el alcance:  
  1) mantener comportamiento del CLI  
  2) agregar cargador de CSV  
  3) agregar pruebas  
  4) convertir a un paquete pequeño

<!-- Fin del archivo -->