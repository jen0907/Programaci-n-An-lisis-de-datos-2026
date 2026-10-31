"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

provincias = set()
pendientes = 0 

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
tiempo_atencion = 0

casos = {
    "Acceso": 0, "Equipo": 0, "Red": 0  
}
casos_urgentes = []
caso_mas_largo = None
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for incidencia in incidencias:
    tiempo_atencion += incidencia["minutos_atencion"]
    casos[incidencia["categoria"]] += 1
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
    if incidencia["resuelto"] == False:
        pendientes += 1
        provincias.add(incidencia["provincia"])
        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))
    if caso_mas_largo is None:
        caso_mas_largo = (incidencia["id"], incidencia["minutos_atencion"])
    elif incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (incidencia["id"], incidencia["minutos_atencion"])
promedio_minutos = tiempo_atencion / len(incidencias)
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
print(
    f"Total de minutos: {tiempo_atencion}\n"
    f"Promedio de minutos: {promedio_minutos:.2f}\n"
    f"Acceso: {casos['Acceso']}\n"
    f"Equipo: {casos['Equipo']}\n"
    f"Red: {casos['Red']}\n"
    f"Casos pendientes: {pendientes}\n"
    f"Provincias con pendientes: {provincias}\n"
    f"¿San Jose tiene casos pendientes?: {'San Jose' in provincias}\n"
    f"Casos urgentes: {casos_urgentes}\n"
    f"Caso con más minutos de atención: {caso_mas_largo}")
