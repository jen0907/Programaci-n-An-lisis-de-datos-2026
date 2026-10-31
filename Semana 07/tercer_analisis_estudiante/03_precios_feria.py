"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio_precios = sum(precios) / len(precios)
precio_minimo = min(precios)
precio_maximo = max(precios)
rango_precios = max(precios) - min(precios)
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0
precios_superiores = 0
while indice < len(precios):
    
    if precios[indice] > promedio_precios:
        precios_superiores += 1
    indice += 1
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango_precios >= 300:
    clasificacion = "Variación alta"
elif rango_precios >= 150:
    clasificacion = "Moderada"
else:
    clasificacion = "Baja"
# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
print(f"Producto: {producto} \nPromedio: {promedio_precios} \nMinimo: {precio_minimo} \nMaximo: {precio_maximo} \nRango: {rango_precios} \nCantidad de precios superiores: {precios_superiores} \nClasificación: {clasificacion}")