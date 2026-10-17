producto = ["Cafe", 5000, 20]

porcentaje_aumento = 20

descuento = producto[1] * 15 / 100

ingreso_actual = producto[1] * producto[2] 

precio_promocional = producto[1] - descuento


aumento = producto[2] * porcentaje_aumento / 100

aumento_unidad = aumento + 20

unidades_totales = aumento_unidad + producto[2]

ingreso_proyectado = precio_promocional * aumento_unidad

diferencia = ingreso_proyectado - ingreso_actual

if diferencia > 0:
    RECOMENDACIÓN = "Lanzar"
else:
    RECOMENDACIÓN = "No Lanzar"
print(RECOMENDACIÓN)







