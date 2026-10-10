#Solución: Misión de Kit seguro

nombre = input("Nombre: ").upper().strip()
kit = input('Tipo  de kit: ').lower().strip()
autorizacion = input("¿Tiene autorización (si/no)?: ").lower().strip()
try:
    cantidad = int(input("Cantidad de kits?: "))
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
    
print("-" * 50,'\n')
print(resultado)
