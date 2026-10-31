"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

total_asistencias = 0
bloques_superiores = 0
# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for asistencia in asistencias:
    total_asistencias += asistencia

    if asistencia > 210:
        bloques_superiores += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total_asistencias / len(asistencias)
promedio_capacidad = promedio / capacidad * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if promedio_capacidad >= 80:
    clasificacion = "Alta"
elif promedio_capacidad >= 50:
    clasificacion = "Media"
else:
    clasificacion = "Baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print(f"Total: {total_asistencias}\nPromedio: {promedio}\nPorcentaje:{promedio_capacidad}\nCantidad de bloques: {bloques_superiores}\nEstado: {clasificacion}")