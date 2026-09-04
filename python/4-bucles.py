# Bucle for
# Bucle for básico: contar del 0 al 4
for i in range(5):
    print(f"Iteración número {i}")

# Resultado:
# Iteración número 0
# Iteración número 1
# Iteración número 2
# Iteración número 3
# Iteración número 4

# range(inicio, fin) — desde inicio hasta fin-1
for numero in range(1, 11):
    print(f"{numero} x 7 = {numero * 7}")

# range(inicio, fin, paso) — de 2 en 2
for par in range(0, 20, 2):
    print(par, end=" ")  # 0 2 4 6 8 10 12 14 16 18


# Bucle for con nombres
# Iterar sobre una lista de elementos
frutas = ["manzana", "banana", "cereza", "dátil"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Ejemplo práctico: enviar emails (simulado)
usuarios = ["ana@mail.com", "bob@mail.com", "carlos@mail.com"]

for email in usuarios:
    print(f"Enviando bienvenida a {email}...")
    print(f"  [OK] Email enviado a {email}")

print(f"Proceso completado: {len(usuarios)} emails enviados")


# Bucle for para recorrer un texto
# Recorrer un texto, letra a letra
for letra in "datos":
    print(letra)

# Resultado: d, a, t, o, s — cada una en su línea

# len() funciona también con texto: cuenta las letras
mensaje = "Hola mundo"
print(f"El mensaje tiene {len(mensaje)} caracteres")  # 10 (incluye el espacio)

# .lower() pasa todo a minúscula: útil para comparar sin importar MAY/min
nombre = "ANA García"
print(nombre.lower())  # "ana garcía"