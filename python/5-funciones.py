# ejemplos de funciones
def saludar(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al programa.")

saludar("Susana")
saludar("Cristian")

# Función con RETURN
def calcular_iva(precio, porcentaje_iva=21):
    iva = precio * (porcentaje_iva / 100)
    total = precio + iva
    return total

# Usar el valor devuelto
precio_final = calcular_iva(100)
print(f"100€ + IVA = {precio_final}€")

# Con otro porcentaje de IVA
precio_reducido = calcular_iva(100, 10)
print(f"100€ + IVA reducido = {precio_reducido}€")

# Función que HACE algo (no return)
def mostrar_ticket(producto, precio, cantidad):
    """Imprime un ticket de compra formateado."""
    total = precio * cantidad
    print("=" * 30)
    print(f"Producto: {producto}")
    print(f"Precio unidad: {precio:.2f}€")
    print(f"Cantidad: {cantidad}")
    print(f"TOTAL: {total:.2f}€")
    print("=" * 30)

mostrar_ticket("Café", 1.50, 3)