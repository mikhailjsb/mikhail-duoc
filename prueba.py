import json
import os

archivo = 'inventario_data.json'

def cargar_datos():
    if os.path.exists(archivo):
        with open(archivo, 'r') as file:
            return json.load(file)
    return {}

def guardar_datos(datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

def registrar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in inventario:
        print("El producto ya existe.")
        return
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
        print("Producto registrado con éxito.")
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")

def actualizar_inventario(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre not in inventario:
        print("El producto no existe.")
        return
    try:
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        inventario[nombre]['cantidad'] = cantidad
        print("Cantidad actualizada con éxito.")
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")

def mostrar_inventario(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
        return
    for nombre, detalles in inventario.items():
        print(f"Nombre: {nombre}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")

def main():
    inventario = cargar_datos()
    while True:
        print("\nControl de Inventario")
        print("1. Registrar productos")
        print("2. Actualizar inventario")
        print("3. Mostrar inventario")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_producto(inventario)
        elif opcion == '2':
            actualizar_inventario(inventario)
        elif opcion == '3':
            mostrar_inventario(inventario)
        elif opcion == '4':
            guardar_datos(inventario)
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()