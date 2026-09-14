# Crear y modificar listas
productos_stock = ["laptop", "monitor", "teclado", "ratón"]


# Añadir elementos
productos_stock.append("webcam")           # Añade al final
productos_stock.insert(0, "servidor")      # Inserta en posición 0


# Eliminar elementos
productos_stock.remove("ratón")            # Elimina por valor
eliminado = productos_stock.pop()          # Elimina y devuelve el último


# Longitud
print(f"Productos en stock: {len(productos_stock)}")


# Ordenar
precios = [299.99, 49.99, 899.00, 129.50, 1499.00]
precios.sort()                  # Ordena la lista original (in-place)
precios_desc = sorted(precios, reverse=True)  # Crea nueva lista ordenada


# Buscar
print("laptop" in productos_stock)  # True o False
print(precios.index(899.00))        # Posición del elemento


### List comprehensions

precios_sin_iva = [100, 250, 49.99, 899, 1299.50] # Precios sin IVA

# Calcular precios con IVA (21%) — SIN list comprehension
precios_con_iva = []
for precio in precios_sin_iva:
    precios_con_iva.append(precio * 1.21)

# Calcular precios con IVA (21%) — CON list comprehension
precios_con_iva_lc = [precio * 1.21 for precio in precios_sin_iva]

# Filtrar: solo precios mayores a 200€
caros = [precio for precio in precios_con_iva if precio > 200]
print(f"Productos caros (>200€): {caros}")

# Transformar: redondear a 2 decimales
redondeados = [round(precio, 2) for precio in precios_con_iva]
print(f"Redondeados: {redondeados}")


##############################################
# Diccionarios

ventas = [
    {"fecha": "2024-01-15", "producto": "Laptop", "importe": 1299.00},
    {"fecha": "2024-01-15", "producto": "Monitor", "importe": 349.99},
    {"fecha": "2024-01-16", "producto": "Teclado", "importe": 79.99},
    {"fecha": "2024-01-16", "producto": "Laptop", "importe": 1299.00},
    {"fecha": "2024-01-17", "producto": "Ratón", "importe": 29.99},
]

# Filtrar: ventas de más de 100€
grandes = [venta for venta in ventas if venta["importe"] > 100]
print(f"Ventas grandes: {len(grandes)}")

# Transformar: extraer solo importes
importes = [venta["importe"] for venta in ventas]
print(f"Total facturado: {sum(importes):.2f}€")

# Agrupar: ventas por producto
from collections import Counter
productos_vendidos = [venta["producto"] for venta in ventas]
conteo = Counter(productos_vendidos)
print(f"Ventas por producto: {dict(conteo)}")


# Metodos esenciales
cliente = {
    "nombre": "Carlos López",
    "email": "carlos@empresa.com",
    "plan": "premium",
    "gasto_mensual": 450.00,
}

# Obtener todas las claves y valores
print(list(cliente.keys()))    # ["nombre", "email", "plan", "gasto_mensual"]
print(list(cliente.values()))  # ["Carlos López", "carlos@empresa.com", ...]

# Iterar sobre clave-valor (muy común en datos)
for campo, valor in cliente.items():
    print(f"  {campo}: {valor}")

# Actualizar múltiples campos de golpe
cliente.update({"plan": "enterprise", "gasto_mensual": 890.00})

# Eliminar una clave
del cliente["email"]

# Copiar (cuidado: = NO copia, crea una referencia)
cliente_copia = cliente.copy()