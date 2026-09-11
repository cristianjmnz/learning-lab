# Mini proyecto
# Estructura: lista de diccionarios
# Cada gasto es un diccionario con 3 campos: concepto, cantidad y categoría
gastos = [] # Empieza vacío

gasto = {
    "concepto": "Netflix",
    "cantidad": 11.50,
    "categoria": "ocio"
}

gastos.append(gasto) # Añadir el gasto a la lista
#print(gastos[0])

gasto2 = {
    "concepto": "PS Plus",
    "cantidad": 9.99,
    "categoria": "ocio"
}
gastos.append(gasto2)
#print(gastos[1])

for gasto in gastos:
    print(f"Concepto: {gasto['concepto']}, Cantidad: {gasto['cantidad']:.2f}€, Categoría: {gasto['categoria']}")


total = 0
for gasto in gastos:
    total += gasto["cantidad"] # Sumar la cantidad del gasto total

print(f"Total gastado: {total:.2f} €")
