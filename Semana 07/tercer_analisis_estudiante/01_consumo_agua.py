"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.

sum(consumos_litros) / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
consumos_litros[0] - consumos_litros[4] 
reduccion = (consumos_litros[0] - consumos_litros[4]) / consumos_litros [0] * 100
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.

if reduccion >= 15:
    clasificacion = "Reducción alta"
elif reduccion > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"    
    
# Calculo del total y de promedio 
consumo_total = sum(consumos_litros)
promedio_diario = sum(consumos_litros) / len(consumos_litros)
litros_ahorrados = consumos_litros[0] - consumos_litros[4]
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
print(f"Clasificación {clasificacion}\nConsumo total: {consumo_total}L\nPromedio: {promedio_diario}L\nAhorro: {litros_ahorrados}L\nReducción: {reduccion}%")