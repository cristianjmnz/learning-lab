# Input()

# Pedir texto al usuario
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}! Bienvenido al programa.")

# Pedir un número (¡hay que convertirlo!)
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)  # Convertir texto → número entero
print(f"El año que viene tendrás {edad + 1} años")

# Versión compacta: convertir directamente
peso = float(input("¿Cuánto pesas en kg? "))
altura = float(input("¿Cuánto mides en metros? "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.1f}")  # :.1f muestra 1 decimal