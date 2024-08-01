import sqlite3
import os

# Funciones de gestión de la base de datos
def agregar_marca(nombre):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO marca (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()

def listar_marca():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM marca')
    marcas = cursor.fetchall()
    conn.close()
    return marcas

def agregar_categoria(nombre):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categoria (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()


def agregar_estado(nombre):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estado (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()


def agregar_articulo(nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO articulos (nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id))
    conn.commit()
    conn.close()


def listar_articulos():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT articulos.id, articulos.nombre, articulos.cantidad, articulos.ubicacion,
               marca.nombre AS marca, categoria.nombre AS categoria, estado.nombre AS estado
        FROM articulos
        LEFT JOIN marca ON articulos.marca_id = marca.id
        LEFT JOIN categoria ON articulos.categoria_id = categoria.id
        LEFT JOIN estado ON articulos.estado_id = estado.id
    ''')
    articulos = cursor.fetchall()
    conn.close()
    return articulos


def actualizar_articulo(id, nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE articulos
        SET nombre = ?, cantidad = ?, ubicacion = ?, marca_id = ?, categoria_id = ?, estado_id = ?
        WHERE id = ?
    ''', (nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id, id))
    conn.commit()
    conn.close()


def eliminar_articulo(id):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM articulos WHERE id = ?', (id,))
    conn.commit()
    conn.close()


# Interfaz de usuario en la consola
def mostrar_menu():
    print("1. Ingresar artículo")
    print("2. Listar artículos")
    print("3. Actualizar artículo")
    print("4. Eliminar artículo")
    print("6. Agregar categoría")
    print("7. Agregar estado")
    print("8. Salir")
    print("9. AMB de tablas")

def mostrar_menu_2():
    print("1. Alta marca")
    print("2. Baja marcas")
    print("3. Modificar marca")
    print("4. Consultar marca")
    print("5. Volver")

def limpiar_pantalla():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix/Linux/MacOS
    else:
        os.system('clear')

def main():
    #inicializar_bd()
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del artículo: ")
            cantidad = int(input("Cantidad: "))
            ubicacion = input("Ubicación: ")
            marca_id = int(input("ID de la marca: "))
            categoria_id = int(input("ID de la categoría: "))
            estado_id = int(input("ID del estado: "))
            agregar_articulo(nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id)
        elif opcion == '2':
            articulos = listar_articulos()
            for articulo in articulos:
                print(articulo)
        elif opcion == '3':
            id = int(input("ID del artículo a actualizar: "))
            nombre = input("Nuevo nombre del artículo: ")
            cantidad = int(input("Nueva cantidad: "))
            ubicacion = input("Nueva ubicación: ")
            marca_id = int(input("Nuevo ID de la marca: "))
            categoria_id = int(input("Nuevo ID de la categoría: "))
            estado_id = int(input("Nuevo ID del estado: "))
            actualizar_articulo(id, nombre, cantidad, ubicacion, marca_id, categoria_id, estado_id)
        elif opcion == '4':
            id = int(input("ID del artículo a eliminar: "))
            eliminar_articulo(id)
        elif opcion == '6':
            nombre = input("Nombre de la categoría: ")
            agregar_categoria(nombre)
        elif opcion == '7':
            nombre = input("Nombre del estado: ")
            agregar_estado(nombre)
        elif opcion == '8':
            break
        elif opcion == '9':
            limpiar_pantalla()
            while True:
                mostrar_menu_2()
                opcion = input("Seleccione una opción: ")
                if opcion == '1':
                    nombre = input("Nombre de la marca: ")
                    agregar_marca(nombre)
                if opcion == '4':
                    listar_marca()
                if opcion == '5':
                    break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
