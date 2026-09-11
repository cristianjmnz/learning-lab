# Mini proyecto
# PROYECTO COMPLETO: Gestor de Gastos Personales
gastos = []

def mostrar_menu():
    print("")
    print("=" * 35)
    print("  GESTOR DE GASTOS PERSONALES")
    print("=" * 35)
    print("  1. Añadir gasto")
    print("  2. Ver todos los gastos")
    print("  3. Resumen por categoría")
    print("  4. Buscar gastos")
    print("  5. Salir")
    print("-" * 35)

def agregar_gasto(gastos):
    concepto = input("  ¿Qué compraste? ")
    cantidad = float(input("  ¿Cuánto costó? (€): "))
    categoria = input("  Categoría (comida/transporte/ocio/hogar): ").lower()
    gastos.append({"concepto": concepto, "cantidad": cantidad, "categoria": categoria})
    print(f"  [OK] Registrado: {concepto} - {cantidad:.2f}€")

def ver_gastos(gastos):
    if len(gastos) == 0:
        print("  No hay gastos.")
        return
    total = 0
    for i in range(len(gastos)):
        g = gastos[i]
        print(f"  {i+1}. {g['concepto']:<18} {g['cantidad']:>7.2f}€  [{g['categoria']}]")
        total = total + g["cantidad"]
    print(f"  TOTAL: {total:.2f}€")

def resumen_categorias(gastos):
    if len(gastos) == 0:
        print("  No hay gastos.")
        return
    categorias = {}
    for g in gastos:
        cat = g["categoria"]
        if cat in categorias:
            categorias[cat] = categorias[cat] + g["cantidad"]
        else:
            categorias[cat] = g["cantidad"]
    for cat in categorias:
        print(f"  {cat:<15} {categorias[cat]:>8.2f}€")

def buscar_gastos(gastos):
    print("  Buscar por: (1) categoría  (2) importe mínimo")
    tipo = input("  Opción: ")
    encontrados = []
    if tipo == "1":
        cat = input("  ¿Qué categoría? ").lower()
        for g in gastos:
            if g["categoria"] == cat:
                encontrados.append(g)
    elif tipo == "2":
        minimo = float(input("  ¿Importe mínimo? (€): "))
        for g in gastos:
            if g["cantidad"] >= minimo:
                encontrados.append(g)
    if len(encontrados) == 0:
        print("  No se encontraron gastos.")
    else:
        for g in encontrados:
            print(f"    - {g['concepto']}: {g['cantidad']:.2f}€ ({g['categoria']})")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("  Elige (1-5): ")
    if opcion == "1":
        agregar_gasto(gastos)
    elif opcion == "2":
        ver_gastos(gastos)
    elif opcion == "3":
        resumen_categorias(gastos)
    elif opcion == "4":
        buscar_gastos(gastos)
    elif opcion == "5":
        print("  ¡Adiós!")
        break
    else:
        print("  Opción no válida.")
