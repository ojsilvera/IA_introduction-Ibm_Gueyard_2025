"""
Programa de Análisis de Datos - Basado en DOCUMENTACION.md
Autor: ChatGPT (GPT-5)
Fecha: 2025-10-10
Descripción:
Este programa muestra información resumida del proyecto de análisis de datos
según el documento DOCUMENTACION.md. Incluye menú de navegación, pseudocódigo
y sugerencias de mejora asistidas con Copilot.
"""

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Tema, Problema y Solución")
    print("2. Dataset de referencia: fuente, definición, estructura, tipos y escala")
    print("3. Pseudocódigo y diagrama ASCII del programa")
    print("4. Sugerencias y mejoras aplicadas con Copilot")
    print("0. Salir")
    return input("Seleccione una opción: ")

def opcion_1():
    print("""
=== 1. TEMA, PROBLEMA Y SOLUCIÓN ===

TEMA:
Optimización del surtido de productos y estrategias de fidelización mediante
el análisis integrado de ventas, clientes y categorías de productos.

PROBLEMA:
La empresa enfrenta inconsistencias en la clasificación de productos (bebidas y
alimentos clasificados como limpieza, y viceversa) y necesita integrar la
información de clientes, ventas y productos para optimizar su gestión comercial
y de fidelización.

SOLUCIÓN PROPUESTA:
1. Normalizar las bases de datos eliminando columnas redundantes.
2. Reclasificar correctamente las categorías en productos.csv.
3. Analizar métricas de rentabilidad, frecuencia y valor de cliente (modelo RFM).
4. Integrar visualizaciones y dashboards para la toma de decisiones.
5. Implementar reglas de clasificación y análisis cruzado entre productos.
""")

def opcion_2():
    print("""
=== 2. DATASET DE REFERENCIA ===

FUENTE:
Los datos provienen de cuatro archivos CSV: clientes.csv, ventas.csv,
detalle_ventas.csv y productos.csv.

DEFINICIÓN:
La base representa el registro de clientes, transacciones, productos y detalles
de venta, permitiendo un análisis integral del comportamiento de compra.

ESTRUCTURA Y TIPO DE DATOS:

1. clientes.csv
   - id_cliente (Entero, Razón)
   - nombre_cliente (Texto, Nominal)
   - email (Texto, Nominal)
   - ciudad (Texto, Nominal)
   - fecha_alta (Fecha, Intervalo)

2. ventas.csv
   - id_venta (Entero, Razón)
   - fecha (Fecha, Intervalo)
   - id_cliente (Entero, Razón)
   - medio_pago (Texto, Nominal)
   Recomendación: eliminar columnas redundantes (nombre_cliente, email).

3. detalle_ventas.csv
   - id_venta (Entero, Razón)
   - id_producto (Entero, Razón)
   - cantidad (Entero, Razón)
   - precio_unitario (Numérico, Razón)
   - importe (Numérico, Razón)

4. productos.csv
   - id_producto (Entero, Razón)
   - nombre_producto (Texto, Nominal)
   - categoria (Texto, Nominal)
   - precio_unitario (Numérico, Razón)
   *Errores detectados*: Clasificación incorrecta de categorías.

ESCALA DE MEDICIÓN:
Nominal, Intervalo y Razón según el tipo de variable. Las fechas usan escala de intervalo.
""")

def opcion_3():
    print("""
=== 3. PSEUDOCÓDIGO Y DIAGRAMA ASCII ===

PSEUDOCÓDIGO:
-----------------------------------------
Inicio
    Mostrar menú principal
    Mientras opción != 0 hacer
        Si opción == 1 entonces
            Mostrar tema, problema y solución
        Si opción == 2 entonces
            Mostrar información del dataset
        Si opción == 3 entonces
            Mostrar pseudocódigo y diagrama
        Si opción == 4 entonces
            Mostrar sugerencias y mejoras
        Si opción == 0 entonces
            Terminar programa
        Fin Si
        Mostrar menú nuevamente
    Fin Mientras
Fin
-----------------------------------------

DIAGRAMA ASCII:
-----------------------------------------
     ┌────────────────────────┐
     │     MENÚ PRINCIPAL     │
     └──────────┬─────────────┘
                │
     ┌──────────┼──────────┬───────────┬───────────┐
     │          │          │           │           │
┌────▼────┐┌────▼────┐┌────▼────┐┌────▼────┐┌─────▼────┐
│  Opción ││  Opción ││  Opción ││  Opción ││  Opción  │
│    1    ││    2    ││    3    ││    4    ││    0     │
│  Tema   ││ Dataset ││Pseudo+  ││Mejoras  ││ Salir    │
│Problema ││Referencia││Diagrama││Copilot  ││ Programa │
└─────────┘└─────────┘└────────┘└─────────┘└──────────┘
-----------------------------------------
""")

def opcion_4():
    print("""
=== 4. SUGERENCIAS Y MEJORAS APLICADAS CON COPILOT ===

1. **Documentación mejorada**: Se añadieron docstrings y comentarios descriptivos.
2. **Menú dinámico**: Copilot sugirió simplificar el bucle principal con una estructura clara.
3. **Control de flujo optimizado**: Uso de `match-case` (Python 3.10+) podría aplicarse en versiones modernas.
4. **Estandarización**: Variables, funciones y bloques siguen un formato PEP8.
5. **Escalabilidad**: El código puede ampliarse para leer archivos CSV y realizar análisis reales.
6. **Legibilidad**: Espaciado y encabezados claros en la interfaz de texto.
7. **Posible mejora futura**:
   - Añadir un submenú de visualización con `matplotlib` o `pandas`.
   - Implementar análisis automatizado de errores en categorías.
   - Exportar resultados a un informe PDF.
""")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            opcion_4()
        elif opcion == "0":
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


main()
