# Este script analiza un conjunto de datos de ventas y genera un archivo Excel con varios informes.

import pandas as pd

ventas = [
    {"fecha": "2024-02-01", "producto": "It - Stephen King", "cantidad": 3, "precio": 20.0},
    {"fecha": "2024-02-01", "producto": "La ética protestante - Max Weber", "cantidad": 5, "precio": 18.5},
    {"fecha": "2024-02-02", "producto": "Fundación - Isaac Asimov", "cantidad": 4, "precio": 22.0},
    {"fecha": "2024-02-02", "producto": "El resplandor - Stephen King", "cantidad": 2, "precio": 19.0},
    {"fecha": "2024-02-03", "producto": "Economía y sociedad - Max Weber", "cantidad": 1, "precio": 25.0},
    {"fecha": "2024-02-03", "producto": "Yo, robot - Isaac Asimov", "cantidad": 6, "precio": 17.0},
]

# DataFrame con ventas originales
df_ventas = pd.DataFrame(ventas)

# Calculo ingresos totales
df_ventas["ingreso"] = df_ventas["cantidad"] * df_ventas["precio"]
ingresos_totales = df_ventas["ingreso"].sum()

# Producto más vendido
ventas_por_producto = df_ventas.groupby("producto")["cantidad"].sum()
producto_mas_vendido = ventas_por_producto.idxmax()
cantidad_mas_vendida = ventas_por_producto.max()

# Precio promedio por producto
ingresos_y_cantidades = df_ventas.groupby("producto").agg({"ingreso":"sum", "cantidad":"sum"})
ingresos_y_cantidades["precio_promedio"] = ingresos_y_cantidades["ingreso"] / ingresos_y_cantidades["cantidad"]

# Ingresos totales por día
ingresos_por_dia = df_ventas.groupby("fecha")["ingreso"].sum()

# Resumen ventas por producto
resumen_ventas = ingresos_y_cantidades.rename(columns={"cantidad": "cantidad_total", "ingreso": "ingresos_totales"})

# Crear un Excel con pestañas
with pd.ExcelWriter("analisis_ventas.xlsx", engine="openpyxl") as writer:
    # 1. Lista de ventas original
    df_ventas.to_excel(writer, sheet_name="Ventas Originales", index=False)

    # 2. Ingresos totales generados (en una hoja con resumen simple)
    df_ingresos = pd.DataFrame({
        "Descripción": ["Ingresos totales generados", "Producto más vendido", "Cantidad más vendida"],
        "Valor": [ingresos_totales, producto_mas_vendido, cantidad_mas_vendida]
    })
    df_ingresos.to_excel(writer, sheet_name="Ingresos y Producto", index=False)

    # 3. Precio promedio por producto
    precios_promedio = ingresos_y_cantidades[["precio_promedio"]].reset_index()
    precios_promedio.to_excel(writer, sheet_name="Precio Promedio", index=False)

    # 4. Ingresos totales por día
    ingresos_por_dia_df = ingresos_por_dia.reset_index().rename(columns={"ingreso": "ingresos_totales"})
    ingresos_por_dia_df.to_excel(writer, sheet_name="Ingresos por Día", index=False)

    # 5. Resumen ventas por producto
    resumen_ventas_reset = resumen_ventas.reset_index()
    resumen_ventas_reset.to_excel(writer, sheet_name="Resumen Ventas", index=False)

print("Archivo 'analisis_ventas.xlsx' creado exitosamente.")



