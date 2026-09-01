# Crear variables es como poner cosas en cajas con etiqueta
nombre = "Cristian"
edad = 30
altura = 1.70
es_estudiante = True

# Leer variables: usarlas por su nombre
print(nombre)          # Muestra: Cristian
print(edad)            # Muestra: 30
print(es_estudiante)   # Muestra: True

# Usar variables dentro de texto con f-strings
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura}m")


# Tipos de datos simples
# Números: puedes hacer matemáticas con ellos
precio = 29.99
cantidad = 3
total = precio * cantidad
print(f"Total: {total} euros")  # Total: 89.97

# Texto: puedes concatenarlo (pegarlo)
nombre = "Cristian"
apellido = "Jimenez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Booleanos: para decisiones
mayor_de_edad = True
tiene_carnet = False
print(f"¿Mayor de edad? {mayor_de_edad}")

# CUIDADO: "3" + "5" no es 8, ¡es "35"! (concatenación de texto)
resultado_texto = "3" + "5"
resultado_numero = 3 + 5
print(resultado_texto)   # 35 (pegó dos textos)
print(resultado_numero)  # 8  (sumó dos números)


# Operaciones simples
# Operaciones con números
sueldo_mensual = 2500
meses = 12
sueldo_anual = sueldo_mensual * meses
print(f"Sueldo anual: {sueldo_anual} euros")  # 30000

# Operaciones útiles
cuenta = 45.60
personas = 4
por_persona = cuenta / personas
print(f"Cada uno paga: {por_persona} euros")  # 11.4

# El operador % (módulo) da el RESTO de la división
galletas = 10
amigos = 3
sobran = galletas % amigos
print(f"Sobran {sobran} galletas")  # Sobran 1 galleta

# Reasignar: cambiar el contenido de la caja
contador = 0
print(f"Contador: {contador}")  # 0
contador = contador + 1
print(f"Contador: {contador}")  # 1
contador = contador + 1
print(f"Contador: {contador}")  # 2


# podemos dibujar lineas con *
# Multiplicar un texto por un número lo REPITE
linea = "-" * 36
print(linea)          # ------------------------------------ (36 guiones)

igual = "=" * 20
print(igual)          # ==================== (20 signos igual)

# Sirve para enmarcar la salida y que se lea de un vistazo
print("=" * 30)
print("  REPORTE DE VENTAS")
print("=" * 30)