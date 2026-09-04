#
# ejemplo 1: estructura basica

edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("¡Gracias por usar el programa!")

#
# ejemplo 2: multiples condiciones

nota = 7.5

if nota >=9:
    print("Sobresaliente")
elif nota >=7:
    print("Notable")
elif nota >=5:
    print("Aprobado")
else:
    print("Suspenso. Hay que estudiar más.")

#
# Combinar condiciones
edad = 20
tiene_carnet = True

# AND: ambas deben cumplirse
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# OR: al menos una debe cumplirse
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("¡Es fin de semana!")
else:
    print("A trabajar...")

# NOT: invierte la condición
lloviendo = False
if not lloviendo:
    print("Sal sin paraguas")

#
# condiciones anidadas
# ¿Puedes entrar al concierto?
edad = 20
tiene_entrada = "si"

if tiene_entrada == "si":
    if edad >= 18:
        print("Bienvenido al concierto. Barra libre disponible.")
    else:
        print("Bienvenido. Zona sin alcohol.")
else:
    print("Necesitas comprar una entrada primero.")
    print("Taquilla abierta hasta las 22:00.")


#
# Un ejemplo real: ¿Llegas tarde al trabajo?

hora_actual = 8
minutos = 40
transporte = "bus"

# tiempo estimado segun transporte
if transporte == "andando":
    tiempo_viaje = 25
elif transporte == "bus":
    tiempo_viaje = 15
elif transporte == "coche":
    tiempo_viaje = 10
else:
    tiempo_viaje = 20  # valor por defecto

# calcular hora de llegada
llegada_minutos = minutos + tiempo_viaje
llegada_hora = hora_actual
if llegada_minutos >= 60:
    llegada_hora = llegada_hora + 1
    llegada_minutos = llegada_minutos - 60

hora_entrada = 9 # La oficina abre a las 9:00

print(f"LLegarías a las {llegada_hora}:{llegada_minutos:02d}")

if llegada_hora < hora_entrada:
    print("¡Llegas con tiempo de sobra!")
elif llegada_hora == hora_entrada and llegada_minutos == 0:
    print("Llegas justo. ¡Corre!")
else:
    retraso = (llegada_hora - hora_entrada) * 60 + llegada_minutos
    print(f"Llegas {retraso} minutos tarde. Avisa a tu jefe.")



# juego piedra papel tijera
jugador = "papel"
maquina = "piedra"

print("=== PIEDRA, PAPEL O TIJERAS ===")
print(f"Tú: {jugador}")
print(f"Máquina: {maquina}")
print("")

if jugador == maquina:
    resultado = "¡EMPATE! Ambos eligieron lo mismo."
elif jugador == "piedra" and maquina == "tijeras":
    resultado = "¡GANASTE! Piedra aplasta tijeras."
elif jugador == "papel" and maquina == "piedra":
    resultado = "¡GANASTE! Papel envuelve piedra."
elif jugador == "tijeras" and maquina == "papel":
    resultado = "¡GANASTE! Tijeras cortan papel."
else:
    resultado = "PERDISTE. La máquina gana esta ronda."

print(resultado)