#Solución: Misión de Kit seguro

nombre = input("Nombre: ").upper().strip()
kit = input('Tipo  de kit: ').lower().strip()
autorizacion = input("¿Tiene autorización (si/no)?: ").lower().strip()
try:
    cantidad = int(input("Cantidad de kits?: "))
    if cantidad < 1:
        print("Error: La cantidad minima es 1.")
except ValueError:
    print("Cantidad de kits invalida, digite del 1 - 100")
    cantidad = -1 
try:
    dias = int(input("Días de préstamos: "))
except ValueError:
    print("Cantidad de días invalida, digite del 1-100")
    dias = -1

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado: revise los datos ingresados"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}"
else:
    resultado = "Solicitud enviada a revisión"
print("-" * 50,'\n')
print(resultado)
