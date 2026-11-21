"""El mismo expediente, con Pandas y las mismas tres funciones."""
import pandas as pd
from pathlib import Path

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    print("Cantidad:",len(atenciones))
    print(type (atenciones))
    print((atenciones))

def contar_categorias(atenciones):
    print(atenciones['medicamento'].value_counts())
    print(atenciones['hospital'].value_counts())
    print(atenciones['diagnostico'].value_counts())


def concluir(atenciones):
    print("Cantidad de atenciones atendidas: ",atenciones['cedula'].nunique())
    print("Total de minutos de espera: ", atenciones['minutos_espera'].sum())
    print("Promedio de minutos de espera: ", atenciones['minutos_espera'].mean())
    print("Promedio de minutos de espera: ", atenciones['minutos_espera'].min())
    print("Promedio de minutos de espera: ", atenciones['minutos_espera'].max())
    

try:
    atenciones = pd.read_csv (ARCHIVO_CSV)
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
