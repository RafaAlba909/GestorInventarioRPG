from inventory import Inventario
from object import Objeto
import os
import time

# Instancia del inventario
inventario = Inventario(capacidad=5)

# Algunos objetos posibles (en el futuro podrías hacer esto aleatorio)
objetos_disponibles = [
    Objeto("Espada", "Una espada afilada.", "🗡️"),
    Objeto("Poción", "Cura 50 de vida.", "🧪"),
    Objeto("Escudo", "Protección extra.", "🛡️"),
    Objeto("Llave", "Abre puertas misteriosas.", "🗝️"),
    Objeto("Mapa", "Revela zonas ocultas.", "🗺️"),
    Objeto("Antorcha", "Ilumina lugares oscuros.", "🔥"),
]

index_objeto = 0

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona ENTER para continuar...")

def mostrar_menu():
    print("\n" + "="*40)
    print("🎮  GESTOR DE INVENTARIO RPG")
    print("="*40)
    print("1. Ver Inventario")
    print("2. Eliminar Objeto del Inventario")
    print("3. Avanzar y Encontrar Objeto")
    print("4. Salir del Juego")
    print("="*40)

def input_opcion():
    while True:
        opcion = input("Selecciona una opción (1-4): ")
        if opcion in ["1", "2", "3", "4"]:
            return opcion
        else:
            print("Opción no válida. Intenta de nuevo.")

def input_confirmacion(mensaje):
    while True:
        r = input(mensaje + " [S/N]: ").strip().lower()
        if r in ["s", "n"]:
            return r == "s"
        else:
            print("Por favor escribe S o N.")

def ver_inventario():
    limpiar()
    print("🧾 INVENTARIO ACTUAL\n")
    if inventario.esta_vacio():
        print("Tu inventario está vacío.")
    else:
        for i, item in enumerate(inventario.objetos):
            print(f"{i + 1}. {item.emoji} {item.nombre} x{item.cantidad} - {item.descripcion}")
    pausar()

def eliminar_objeto():
    limpiar()
    if inventario.esta_vacio():
        print("No hay objetos que eliminar.")
        pausar()
        return

    ver_inventario()
    try:
        num = int(input("\nNúmero del objeto a eliminar: "))
        if 1 <= num <= len(inventario.objetos):
            eliminado = inventario.objetos[num - 1]
            if input_confirmacion(f"¿Eliminar '{eliminado.nombre}' del inventario?"):
                inventario.eliminar_objeto(eliminado.nombre)
                print(f"'{eliminado.nombre}' eliminado con éxito.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor ingresa un número válido.")
    pausar()

def avanzar():
    global index_objeto
    limpiar()
    if index_objeto >= len(objetos_disponibles):
        print("No hay más objetos por descubrir.")
        pausar()
        return

    obj = objetos_disponibles[index_objeto]
    print(f"🚶 Avanzas por el mapa y encuentras: {obj.emoji} {obj.nombre} - {obj.descripcion}\n")
    if input_confirmacion(f"¿Quieres recoger '{obj.nombre}'?"):
        if inventario.esta_lleno():
            print("❌ Tu inventario está lleno. No puedes recoger más objetos.")
        else:
            inventario.agregar_objeto(obj)
            print(f"'{obj.nombre}' añadido al inventario.")
    else:
        print(f"Ignoraste el '{obj.nombre}'.")
    index_objeto += 1
    pausar()

# Bucle principal
while True:
    limpiar()
    mostrar_menu()
    opcion = input_opcion()

    if opcion == "1":
        ver_inventario()
    elif opcion == "2":
        eliminar_objeto()
    elif opcion == "3":
        avanzar()
    elif opcion == "4":
        print("\nGracias por jugar 🧙‍♂️ ¡Hasta la próxima!")
        break
