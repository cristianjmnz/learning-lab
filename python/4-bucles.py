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

"""
.lower() pone todo en minúscula, 
.upper() pone todo en mayúscula, 
.isdigit() te dice si un carácter es un número 
.isupper() te dice si es mayúscula.
"""


# Bucle while
# comprobar contraseña

password_correcta = "secreto123"
intentos = 0

# Lo que el usuaario va tecleando, simulado
lo_que_teclea = ["1234", "secreto","secreto123"]

password = lo_que_teclea[intentos]

while password != password_correcta:
    intentos = intentos + 1
    if intentos >= 3:
        print("¡Demasiados intentos! Cuenta bloqueada.")
        break # 'break' sale del bucle inmediatamente
    restantes = 3 - intentos
    print(f"Incorrecta. Te quedan {restantes} intentos.")
    password = lo_que_teclea[intentos]
if password == password_correcta:
    print("¡Acceso concedido! Bienvenido.")


"""
### ¿for o while? Cuándo usar cada uno

    USA FOR cuando sabes cuántas veces repetir: "haz esto 10 veces", "para cada usuario en la lista", "para cada número del 1 al 100".
    USA WHILE cuando NO sabes cuántas veces: "pide la contraseña hasta que sea correcta", "lee datos hasta que el usuario escriba salir", "intenta conectar hasta que funcione".
    En la duda, usa for. Es más seguro (no puedes crear un bucle infinito accidentalmente con for).
"""

# Contar cuantos aprobados y suspensos hay
notas = [7.5, 4.0, 4.9, 5.1, 6.0, 3.5, 8.2]
aprobados = 0
suspensos = 0

for nota in notas:
    if nota >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1

print(f"Aprobados: {aprobados}, Suspensos: {suspensos}")

# inicializar → iterar → acumular → resultado

"""
### Resumen

    ▹for recorre una colección o un rango de números. Sabes cuántas veces se repite.
    ▹while repite mientras una condición sea True. No sabes cuántas veces de antemano.
    ▹range(n) genera números del 0 al n-1. range(a, b) va de a hasta b-1.
    ▹break sale del bucle inmediatamente.
    ▹El patrón acumulador: inicializar variable → iterar → acumular → resultado.
    ▹CUIDADO con bucles infinitos: asegúrate de que la condición del while eventualmente sea False.
"""