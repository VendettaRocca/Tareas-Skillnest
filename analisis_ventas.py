# Datos iniciales: lista de diccionarios con ventas
ventas = [
    {"fecha": "2024-02-01", "producto": "It - Stephen King", "cantidad": 3, "precio": 20.0},
    {"fecha": "2024-02-01", "producto": "La ética protestante - Max Weber", "cantidad": 5, "precio": 18.5},
    {"fecha": "2024-02-02", "producto": "Fundación - Isaac Asimov", "cantidad": 4, "precio": 22.0},
    {"fecha": "2024-02-02", "producto": "El resplandor - Stephen King", "cantidad": 2, "precio": 19.0},
    {"fecha": "2024-02-03", "producto": "Economía y sociedad - Max Weber", "cantidad": 1, "precio": 25.0},
    {"fecha": "2024-02-03", "producto": "Yo, robot - Isaac Asimov", "cantidad": 6, "precio": 17.0},
]

# 1. Calcular ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 2. Análisis del producto más vendido (por cantidad)
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

# Producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 3. Promedio de precio por producto
# Diccionario: producto -> (suma de ingresos, cantidad total)
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingresos = venta["precio"] * venta["cantidad"]
    cantidad = venta["cantidad"]
    if producto in precios_por_producto:
        suma_ingresos, suma_cantidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_ingresos + ingresos, suma_cantidades + cantidad)
    else:
        precios_por_producto[producto] = (ingresos, cantidad)

# Calcular precio promedio por producto
precio_promedio_por_producto = {}
for producto, (suma_ingresos, suma_cantidades) in precios_por_producto.items():
    precio_promedio_por_producto[producto] = suma_ingresos / suma_cantidades

# 4. Ventas por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# 5. Resumen de ventas por producto
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio = precio_promedio_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio
    }

# Mostrar resultados

print("Lista de ventas original:")
for v in ventas:
    print(v)
print()

print(f"Ingresos totales generados: {ingresos_totales:.2f}")
print()

print(f"Producto más vendido: {producto_mas_vendido} con {cantidad_mas_vendida} unidades vendidas")
print()

print("Precio promedio por producto:")
for producto, precio in precio_promedio_por_producto.items():
    print(f"  {producto}: ${precio:.2f}")
print()

print("Ingresos totales por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"  {fecha}: ${ingreso:.2f}")
print()

print("Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"  {producto}:")
    print(f"    Cantidad total: {resumen['cantidad_total']}")
    print(f"    Ingresos totales: ${resumen['ingresos_totales']:.2f}")
    print(f"    Precio promedio: ${resumen['precio_promedio']:.2f}")
