# DOCUMENTACIÓN DEL ANÁLISIS DE DATOS

## Problema de Negocio a Resolver

**Optimización del surtido de productos y estrategias de fidelización mediante el análisis integrado de ventas, clientes y categorías de productos.**

### Contexto

La empresa cuenta con cuatro fuentes de datos clave:

- **`clientes.csv`**: Información de 100 clientes, incluyendo nombre, ciudad, email y fecha de alta.
- **`ventas.csv`**: Registro de 120 transacciones con fecha, cliente asociado e información de medio de pago (efectivo, tarjeta, transferencia, QR).
- **`detalle_ventas.csv`**: Desglose de los productos incluidos en cada venta, con cantidad, precio unitario e importe total.
- **`productos.csv`**: Catálogo de 100 productos con su categoría asignada (Alimentos o Limpieza) y precio unitario.

Estos datos permiten realizar un análisis integral del comportamiento de compra, segmentación de clientes y desempeño de productos.

### Observaciones Relevantes en los Datos

- La clasificación de **categorías** en `productos.csv` contiene errores sistemáticos: bebidas (Pepsi, Fanta, Jugo de Naranja), productos lácteos (Queso Rallado, Yogur), snacks (Papas Fritas, Galletitas) y hasta helados están etiquetados como “Limpieza”, mientras que artículos de higiene personal (Shampoo, Desodorante, Crema Dental) aparecen como “Alimentos”.
- Varios clientes realizan **múltiples compras** (ej.: *Olivia Gomez* con 5 compras, *Agustina Flores* con 5, *Bruno Diaz* con 5), lo que permite aplicar modelos de valor de vida del cliente (CLV) y segmentación RFM.
- El **medio de pago** varía entre las 120 transacciones, lo que permite analizar su relación con el ticket promedio, la frecuencia o la ciudad del cliente.

---

## Estructura, Tipo y Escala de Medición de la Base de Datos

### 1. `clientes.csv`

| Columna          | Tipo de Dato | Escala de Medición | Descripción |
|------------------|--------------|--------------------|-------------|
| `id_cliente`     | Entero       | Razón              | Identificador único del cliente. |
| `nombre_cliente` | Texto        | Nominal            | Nombre completo del cliente. |
| `email`          | Texto        | Nominal            | Correo electrónico. |
| `ciudad`         | Texto        | Nominal            | Localidad de residencia (Carlos Paz, Córdoba, Río Cuarto, etc.). |
| `fecha_alta`     | Fecha        | Intervalo          | Fecha de registro del cliente. |

---

### 2. `ventas.csv`

| Columna          | Tipo de Dato | Escala de Medición | Descripción |
|------------------|--------------|--------------------|-------------|
| `id_venta`       | Entero       | Razón              | Identificador único de la transacción. |
| `fecha`          | Fecha        | Intervalo          | Fecha de la venta. |
| `id_cliente`     | Entero       | Razón              | Clave foránea a `clientes.csv`. |
| `nombre_cliente` | Texto        | Nominal            | **Redundante** (ya está en `clientes.csv`). |
| `email`          | Texto        | Nominal            | **Redundante**. |
| `medio_pago`     | Texto        | Nominal            | Valores: `efectivo`, `tarjeta`, `transferencia`, `qr`. |

> **Recomendación**: Eliminar columnas redundantes (`nombre_cliente`, `email`) para normalizar la base.

---

### 3. `detalle_ventas.csv`

| Columna            | Tipo de Dato | Escala de Medición | Descripción |
|--------------------|--------------|--------------------|-------------|
| `id_venta`         | Entero       | Razón              | Clave foránea a `ventas.csv`. |
| `id_producto`      | Entero       | Razón              | Clave foránea a `productos.csv`. |
| `nombre_producto`  | Texto        | Nominal            | **Redundante** (ya está en `productos.csv`). |
| `cantidad`         | Entero       | Razón              | Unidades vendidas (≥1). |
| `precio_unitario`  | Numérico     | Razón              | Precio por unidad al momento de la venta. |
| `importe`          | Numérico     | Razón              | `cantidad × precio_unitario`. |

> **Recomendación**: Conservar solo `id_producto` y unir con `productos.csv` para obtener el nombre.

---

### 4. `productos.csv`

| Columna            | Tipo de Dato | Escala de Medición | Descripción |
|--------------------|--------------|--------------------|-------------|
| `id_producto`      | Entero       | Razón              | Identificador único del producto. |
| `nombre_producto`  | Texto        | Nominal            | Nombre del producto. |
| `categoria`        | Texto        | Nominal            | Valores: `"Alimentos"` o `"Limpieza"` (**con errores de clasificación**). |
| `precio_unitario`  | Numérico     | Razón              | Precio de lista del producto. |

> **Error crítico**: La columna `categoria` está mal asignada. Ejemplos:
> - **Productos clasificados como “Limpieza” pero son alimentos**:  
>   `Pepsi`, `Fanta`, `Jugo de Naranja`, `Queso Rallado`, `Papas Fritas`, `Helado`, `Fernet`, `Whisky`, etc.
> - **Productos clasificados como “Alimentos” pero son de higiene**:  
>   `Shampoo`, `Desodorante`, `Crema Dental`, `Toallas Húmedas`, `Limpiavidrios`, etc.
>
> **Acción requerida**: Reclasificar manualmente o mediante reglas lógicas antes de cualquier análisis por categoría.

---

## Objetivos del Análisis

1. **Corregir la clasificación de categorías** en `productos.csv` para asegurar la validez de los reportes.
2. **Identificar los productos y categorías más rentables** en términos de ingresos totales y frecuencia de venta.
3. **Segmentar clientes** mediante el modelo RFM (Recencia, Frecuencia, Valor Monetario) y por ciudad.
4. **Analizar el impacto del medio de pago** en el comportamiento del cliente (ej.: ¿el QR se asocia con tickets más altos?).
5. **Detectar patrones de compra cruzada** (market basket analysis) para diseñar promociones efectivas (ej.: Fernet + Coca Cola).

### Beneficios Esperados

- Mejora en la precisión de reportes comerciales.
- Optimización del surtido y gestión de inventario.
- Campañas de marketing segmentadas y personalizadas.
- Aumento de ventas mediante estrategias de cross-selling.
- Corrección de errores en la base de productos, evitando decisiones erróneas.

### Próximos Pasos Técnicos

1. **Normalizar la base**: eliminar redundancias en `ventas.csv` y `detalle_ventas.csv`.
2. **Reclasificar `categoria`** en `productos.csv` usando una regla lógica o diccionario manual.
3. **Unir tablas** mediante claves primarias/foráneas para crear una tabla de hechos de ventas.
4. **Calcular métricas clave**:
   - Ingresos por producto, categoría, cliente y ciudad.
   - Ticket promedio por medio de pago.
   - Frecuencia de compra por cliente.
5. **Generar visualizaciones** y dashboards para apoyar la toma de decisiones.

Nota: Toda esta informacion la genere en base a un curso que tome sobre Aplicaciones de soluciones a negocios con Knime.
---