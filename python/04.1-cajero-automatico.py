# Mini cajero automatico
saldo = 1200.00

# Lo que el ususario va tecleando, simulado
acciones = ["consultar", "retirar", "ingresar", "salir"]
cantidades = [0, 220.0, 20.0, 0]

print("=== CAJERO TRADEREPUBLIC ===")
print(f"Saldo actual: {saldo:.2f} €")

turno = 0
opcion = " "
while opcion != "salir":
    opcion = acciones[turno]
    print(" ")
    print("Opciones: consultar / retirar / ingresar / salir")
    print(f"¿Qué deseas hacer? {opcion}")

    if opcion == "consultar":
        print(f"Tu saldo es: {saldo:.2f}€")
    elif opcion == "retirar":
        cantidad = cantidades[turno]
        if cantidad > saldo:
            print("¡Saldo insuficiente!")
        else:
            saldo = saldo - cantidad
            print(f"Retirados {cantidad:.2f}€. Nuevo saldo: {saldo:.2f}€")
    elif opcion == "ingresar":
        cantidad = cantidades[turno]
        saldo = saldo + cantidad
        print(f"Ingresados {cantidad:.2f}€. Nuevo saldo: {saldo:.2f}€")
    elif opcion == "salir":
        print("¡Hasta luego! Recoge tu tarjeta.")

    turno = turno + 1

# Cambia la lista de acciones y vuelve a ejecutar: el bucle se adapta solo.
# Y fíjate: si quitas "salir" del final, el bucle no termina nunca.