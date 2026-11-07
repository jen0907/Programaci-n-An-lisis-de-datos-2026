"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()

print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
#cada calve es un nombre de medicamento y su valor es el nombre estandarizado 

equivalencias = {
    "acetaminofen" : "acetaminofén", 
    "paracetamol" : "acetaminofén", 
    "antiacido" : "antiácido",
    "lorsartan" : "lorsartán"
}

conteo_medicamentos = {}
total_medicamentos = 0

print("\n ANALISISI FASE #1 MUESTRA 3")
for indice in range (3):
    registro = registros[indice]
    print(f"\nCédula: {registro['paciente_cedula']}"
        f"\nPaciente: {registro['paciente_nombre']}"
        f"\nDiagnostico: {registro['diagnostico']}"
        f"\nMedicamentos: {registro['medicamentos']}") # cedula, nombre, diagnostico, medicamenos -> type 
    
    for medicamento in registro['medicamentos']:
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
    print("\nTotal de medicamentos recetados: " , total_medicamentos)
    print(conteo_medicamentos)
        
    
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\n ANALISIS FASE #2 MEDICAMENTOS DE ATENCIONES")
conteo_medicamentos = {}
total_medicamentos = 0

for registro in registros:
    for medicamento in registro['medicamentos']:
        #limpieza PARACETAMOL -> acetaminofen 
            medicamento = medicamento.strip().lower()
            if medicamento in equivalencias:
                medicamento = equivalencias[medicamento]
            #Contar medicamentos 
            total_medicamentos += 1
            if medicamento in conteo_medicamentos:
                conteo_medicamentos[medicamento] += 1
            else:
                conteo_medicamentos[medicamento] = 1
                
print("\nTotal de medicamentos recetados: " , total_medicamentos)
for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}: \t{cantidad}")

# FASE 3: CONTAR ATENCIONES POR HOSPITAL
conteo_hospital = {}
total_pacientes = 0

for registro in registros:
    total_pacientes += 1  
    hospital = registro['hospital']
    if hospital not in conteo_hospital:
        conteo_hospital[hospital] = 0
    conteo_hospital [hospital] += 1
for hospital in conteo_hospital.items():
    print(f"- {hospital}: \t{cantidad}")
    print("TOTAL PACIENTES: ",total_pacientes)
    
# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

conteo_enfermedades = {}
total_enfermedades = 0

for registro in registros:
    enfermedad = registro['diagnostico']
    total_enfermedades += 1

    if enfermedad not in conteo_enfermedades:
        conteo_enfermedades[enfermedad] = 0

    conteo_enfermedades[enfermedad] += 1

print("\nATENCIONES POR ENFERMEDAD:")
print("TOTAL DE ATENCIONES: ", total_enfermedades)

for enfermedad, cantidad in conteo_enfermedades.items():
    print(f"- {enfermedad}: \t{cantidad}")