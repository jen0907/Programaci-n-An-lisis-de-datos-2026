
ventas = [
    {"vendedor": "Ana", "producto": "Laptop", "categoria": "tecnologia", "precio": 350000},
    {"vendedor": "Luis", "producto": "Mouse", "categoria": "accesorios", "precio": 8500},
    {"vendedor": "Ana", "producto": "Teclado", "categoria": "accesorios", "precio": 15000},
    {"vendedor": "Pedro", "producto": "Laptop", "categoria": "tecnologia", "precio": 350000},
    {"vendedor": "Luis", "producto": "Monitor", "categoria": "tecnologia", "precio": 125000},
    {"vendedor": "Ana", "producto": "Mouse", "categoria": "accesorios", "precio": 8500}
]

# FASE 1: CONTAR VENTAS POR VENDEDOR

conteo_vendedores = {}

for venta in ventas:
    vendedor = venta["vendedor"]

    if vendedor not in conteo_vendedores:
        conteo_vendedores[vendedor] = 0

    conteo_vendedores[vendedor] += 1

print("\nVENTAS POR VENDEDOR")

for vendedor, cantidad in conteo_vendedores.items():
    print(f"{vendedor}: {cantidad}")


# FASE 2: CALCULAR INGRESOS TOTALES

total_ingresos = 0

for venta in ventas:
    total_ingresos += venta["precio"]
    

print("\nINGRESOS TOTALES:", total_ingresos)


# FASE 3: CONTAR PRODUCTOS POR CATEGORIA

conteo_categorias = {}

for venta in ventas:
    categoria = venta["categoria"]

    if categoria not in conteo_categorias:
        conteo_categorias[categoria] = 1

    conteo_categorias[categoria] += 1

print("\nPRODUCTOS POR CATEGORIA")

for categoria, cantidad in conteo_categorias.items():
    print(f"{categoria}: {cantidad}")


# FASE 4: IDENTIFICAR VENTAS MAYORES A 100000

print("\nVENTAS MAYORES A 100000")

for venta in ventas:
    if venta["precio"] > 100000:
        print(venta["producto"], venta["precio"])

print("INFORME DE VENTAS\n")
print(f"Vendedor:\t  {venta['vendedor']}")
print(f"Producto: \t {venta['producto']}")
print(f"Precio:\t\t {venta['precio']}")