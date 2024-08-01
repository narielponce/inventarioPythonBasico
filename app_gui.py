import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

def inicializar_bd():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS marca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ubicacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articulos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        marca_id INTEGER,
        modelo TEXT,
        serial_number TEXT,
        categoria_id INTEGER,
        estado_id INTEGER,
        FOREIGN KEY (marca_id) REFERENCES marca(id),
        FOREIGN KEY (categoria_id) REFERENCES categoria(id),
        FOREIGN KEY (estado_id) REFERENCES estado(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingresos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE NOT NULL,
        articulo_id INTEGER,
        cantidad INTEGER NOT NULL,
        ubicacion_id INTEGER,
        remito TEXT,
        FOREIGN KEY (articulo_id) REFERENCES articulo(id),
        FOREIGN KEY (ubicacion_id) REFERENCES ubicacion(id)
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            articulo_id INTEGER,
            cantidad INTEGER NOT NULL,
            ubicacion_id INTEGER,
            FOREIGN KEY (articulo_id) REFERENCES articulo(id),
            FOREIGN KEY (ubicacion_id) REFERENCES ubicacion(id)
        )
        ''')

    conn.commit()
    conn.close()
def obtener_articulos():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, modelo, serial_number FROM articulos')
    articulos = cursor.fetchall()
    conn.close()
    return articulos
def obtener_marcas():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM marca')
    marcas = cursor.fetchall()
    conn.close()
    return marcas
def obtener_categorias():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM categoria')
    categorias = cursor.fetchall()
    conn.close()
    return categorias
def obtener_estados():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM estado')
    estados = cursor.fetchall()
    conn.close()
    return estados
def obtener_ubicacaciones():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM ubicacion')
    ubicaciones = cursor.fetchall()
    conn.close()
    return ubicaciones
def agregar_marca(nombre):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO marca (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()
def listar_marcas():
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
def listar_categorias():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categoria')
    categorias = cursor.fetchall()
    conn.close()
    return categorias
def agregar_estado(nombre):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estado (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()
def listar_estados():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estado')
    estados = cursor.fetchall()
    conn.close()
    return estados
def agregar_articulo(nombre, modelo, serial_number, marca_id, categoria_id, estado_id):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO articulos (nombre, modelo, serial_number, marca_id, categoria_id, estado_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, modelo, serial_number, marca_id, categoria_id, estado_id))
    conn.commit()
    conn.close()

def agregar_ingreso(fecha, cantidad, articulo_id, ubicacion_id, remito):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ingresos (fecha, cantidad, articulo_id, ubicacion_id, remito)
        VALUES (?, ?, ?, ?, ?)
    ''', (fecha, cantidad, articulo_id, ubicacion_id, remito))
    conn.commit()
    conn.close()
def listar_articulos():
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT articulos.id, articulos.nombre, articulos.modelo, articulos.serial_number, marca.nombre AS marca, categoria.nombre AS categoria, estado.nombre AS estado
        FROM articulos
        LEFT JOIN marca ON articulos.marca_id = marca.id
        LEFT JOIN categoria ON articulos.categoria_id = categoria.id
        LEFT JOIN estado ON articulos.estado_id = estado.id
    ''')
    articulos = cursor.fetchall()
    conn.close()
    return articulos
def actualizar_articulo(id, nombre, ubicacion, marca_id, categoria_id, estado_id):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE articulos
        SET nombre = ?, ubicacion = ?, marca_id = ?, categoria_id = ?, estado_id = ?
        WHERE id = ?
    ''', (nombre, ubicacion, marca_id, categoria_id, estado_id, id))
    conn.commit()
    conn.close()
def eliminar_articulo(id):
    conn = sqlite3.connect('deposito.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM articulos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
def limpiar_pantalla():
    for widget in root.winfo_children():
        widget.destroy()

# Funciones de la GUI
def mostrar_menu():
    limpiar_pantalla()

    tit1 = ttk.Label(root, text="Maestro de artículos", font=("Helvetica", 14))
    tit1.pack(pady=5)

    ttk.Button(root, text="Listado Maestro de artículos", command=listar_articulos_gui).pack(pady=10)
    ttk.Button(root, text="Alta nuevo artículo", command=agregar_articulo_gui).pack(pady=10)

    # Crear un widget Canvas
    canvas = tk.Canvas(root, width=600, height=2, bg='white')
    canvas.pack(pady=5)

    tit2 = ttk.Label(root, text="Operaciones", font=("Helvetica", 14))
    tit2.pack(pady=5)

    ttk.Button(root, text="Retiro de material").pack(pady=10)
    ttk.Button(root, text="Ingreso de material", command=agregar_ingreso_material_gui).pack(pady=10)
    ttk.Button(root, text="Visualización de inventario").pack(pady=10)

    canvas = tk.Canvas(root, width=600, height=2, bg='white')
    canvas.pack(pady=5)

    tit3 = ttk.Label(root, text="Tablas auxiliares", font=("Helvetica", 14))
    tit3.pack(pady=5)

    #ttk.Button(root, text="Actualizar artículo", command=actualizar_articulo_gui).pack(pady=10)
    #ttk.Button(root, text="Eliminar artículo", command=eliminar_articulo_gui).pack(pady=10)

    ttk.Button(root, text="Agregar marca", command=agregar_marca_gui).pack(pady=10)
    ttk.Button(root, text="Listar marcas", command=listar_marcas_gui).pack(pady=10)

    ttk.Button(root, text="Agregar categoría", command=agregar_categoria_gui).pack(pady=10)
    ttk.Button(root, text="Listar categorías", command=listar_categorias_gui).pack(pady=10)

    ttk.Button(root, text="Agregar estado", command=agregar_estado_gui).pack(pady=10)
    ttk.Button(root, text="Listar estados", command=listar_estados_gui).pack(pady=10)

    canvas = tk.Canvas(root, width=600, height=2, bg='white')
    canvas.pack(pady=5)

    tit2 = ttk.Label(root, text="Salir del sistema", font=("Helvetica", 14))
    tit2.pack(pady=5)

    ttk.Button(root, text="Salir", command=root.quit).pack(pady=10)
def agregar_articulo_gui():
    limpiar_pantalla()

    ttk.Label(root, text="Nombre del artículo:").pack(pady=5)
    nombre = ttk.Entry(root)
    nombre.pack(pady=5)

    ttk.Label(root, text="Modelo:").pack(pady=5)
    modelo = ttk.Entry(root)
    modelo.pack(pady=5)

    ttk.Label(root, text="Número de serie:").pack(pady=5)
    serial_number = ttk.Entry(root)
    serial_number.pack(pady=5)

    marcas = obtener_marcas()
    categorias = obtener_categorias()
    estados = obtener_estados()

    ttk.Label(root, text="Marca:").pack(pady=5)
    marca_cb = ttk.Combobox(root, values=[f"{marca[1]} (ID: {marca[0]})" for marca in marcas])
    marca_cb.pack(pady=5)

    ttk.Label(root, text="Categoría:").pack(pady=5)
    categoria_cb = ttk.Combobox(root, values=[f"{categoria[1]} (ID: {categoria[0]})" for categoria in categorias])
    categoria_cb.pack(pady=5)

    ttk.Label(root, text="Estado:").pack(pady=5)
    estado_cb = ttk.Combobox(root, values=[f"{estado[1]} (ID: {estado[0]})" for estado in estados])
    estado_cb.pack(pady=5)

    def guardar():
        marca_id = int(marca_cb.get().split("ID: ")[1][:-1])
        categoria_id = int(categoria_cb.get().split("ID: ")[1][:-1])
        estado_id = int(estado_cb.get().split("ID: ")[1][:-1])

        agregar_articulo(nombre.get(), modelo.get(), serial_number.get(), marca_id, categoria_id, estado_id)
        messagebox.showinfo("Información", "Artículo agregado con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)
def listar_articulos_gui():
    limpiar_pantalla()
    #articulos = listar_articulos()

    #for articulo in articulos:
    #    ttk.Label(root, text=str(articulo)).pack(pady=5)

    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("ID", "Nombre", "Modelo", "N° Serie", "Marca", "Categoría", "Estado"),
                        show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Modelo", text="Modelo")
    tree.heading("N° Serie", text="N° Serie")
    tree.heading("Marca", text="Marca")
    tree.heading("Categoría", text="Categoría")
    tree.heading("Estado", text="Estado")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)
    tree.column("Modelo", width=100, anchor=tk.W)
    tree.column("N° Serie", width=150, anchor=tk.W)
    tree.column("Marca", width=100, anchor=tk.W)
    tree.column("Categoría", width=100, anchor=tk.W)
    tree.column("Estado", width=100, anchor=tk.W)

    # Agregar los artículos al Treeview
    for articulo in listar_articulos():
        tree.insert("", tk.END, values=articulo)

    tree.pack(pady=20)

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)
def listar_marcas_gui():
    limpiar_pantalla()
    #marcas = listar_marcas()

    #for marca in marcas:
    #    ttk.Label(root, text=str(marca)).pack(pady=5)

    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("ID", "Nombre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)

    # Agregar los artículos al Treeview
    for marca in listar_marcas():
        tree.insert("", tk.END, values=marca)

    tree.pack(pady=10)

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)
def listar_categorias_gui():
    limpiar_pantalla()
    #categorias = listar_categorias()

    #for categoria in categorias:
    #    ttk.Label(root, text=str(categoria)).pack(pady=5)

    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("ID", "Nombre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)

    # Agregar las categorías al Treeview
    for categoria in listar_categorias():
        tree.insert("", tk.END, values=categoria)

    tree.pack(pady=10)

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)
def listar_estados_gui():
    limpiar_pantalla()
    #estados = listar_estados()

    #for estado in estados:
    #    ttk.Label(root, text=str(estado)).pack(pady=5)

    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("ID", "Nombre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)

    # Agregar los estados al Treeview
    for estado in listar_estados():
        tree.insert("", tk.END, values=estado)

    tree.pack(pady=10)

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)

def actualizar_articulo_gui():
    limpiar_pantalla()

    ttk.Label(root, text="ID del artículo a actualizar:").pack(pady=5)
    id = ttk.Entry(root)
    id.pack(pady=5)

    ttk.Label(root, text="Nuevo nombre del artículo:").pack(pady=5)
    nombre = ttk.Entry(root)
    nombre.pack(pady=5)

    ttk.Label(root, text="Nueva ubicación:").pack(pady=5)
    ubicacion = ttk.Entry(root)
    ubicacion.pack(pady=5)

    ttk.Label(root, text="Nuevo ID de la marca:").pack(pady=5)
    marca_id = ttk.Entry(root)
    marca_id.pack(pady=5)

    ttk.Label(root, text="Nuevo ID de la categoría:").pack(pady=5)
    categoria_id = ttk.Entry(root)
    categoria_id.pack(pady=5)

    ttk.Label(root, text="Nuevo ID del estado:").pack(pady=5)
    estado_id = ttk.Entry(root)
    estado_id.pack(pady=5)

    def actualizar():
        actualizar_articulo(int(id.get()), nombre.get(), ubicacion.get(), int(marca_id.get()),
                            int(categoria_id.get()), int(estado_id.get()))
        messagebox.showinfo("Información", "Artículo actualizado con éxito")
        mostrar_menu()

    ttk.Button(root, text="Actualizar", command=actualizar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)

def eliminar_articulo_gui():
    limpiar_pantalla()

    ttk.Label(root, text="ID del artículo a eliminar:").pack(pady=5)
    id = ttk.Entry(root)
    id.pack(pady=5)

    def eliminar():
        eliminar_articulo(int(id.get()))
        messagebox.showinfo("Información", "Artículo eliminado con éxito")
        mostrar_menu()

    ttk.Button(root, text="Eliminar", command=eliminar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)
def agregar_marca_gui():
    limpiar_pantalla()

    ttk.Label(root, text="Nombre de la marca:").pack(pady=5)
    nombre = ttk.Entry(root)
    nombre.pack(pady=5)

    def guardar():
        agregar_marca(nombre.get())
        messagebox.showinfo("Información", "Marca agregada con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)
def agregar_ingreso_material_gui():
    limpiar_pantalla()

    articulos = obtener_articulos()
    ubicaciones = obtener_ubicacaciones()
    marcas = obtener_marcas()
    categorias = obtener_categorias()
    estados = obtener_estados()

    # Crear etiqueta y campo de entrada para la fecha
    ttk.Label(root, text="Fecha ingreso material (DD/MM/YYYY):").pack(pady=10)
    fecha_entry = ttk.Entry(root)
    fecha_entry.pack(pady=5)

    ttk.Label(root, text="Cantidad:").pack(pady=5)
    cantidad = ttk.Entry(root)
    cantidad.pack(pady=5)

    ttk.Label(root, text="Artículo:").pack(pady=5)
    articulo_cb = ttk.Combobox(root, width=60, values=[
        f"ID: {articulo[0]} - {articulo[1]} - Mod: {articulo[2]} - SN: {articulo[3]})"
        for articulo in articulos])
    articulo_cb.pack(pady=5)

    ttk.Label(root, text="Ubicación:").pack(pady=5)
    ubicacion_cb = ttk.Combobox(root, values=[f"{ubicacion[1]} (ID: {ubicacion[0]})" for ubicacion in ubicaciones])
    ubicacion_cb.pack(pady=5)

    ttk.Label(root, text="N° Remito / Proveedor:").pack(pady=5)
    num_remito = ttk.Entry(root)
    num_remito.pack(pady=5)

    def guardar():
        #articulo_id = int(articulo_cb.get().split("ID: ")[1][:-1])
        #articulo_id = int(articulo_cb.get().split("ID: ")[0])
        articulo_id = int(articulo_cb.get().split("ID: ")[1].split()[0])
        ubicacion_id = int(ubicacion_cb.get().split("ID: ")[1][:-1])

        agregar_ingreso(fecha_entry.get(), cantidad.get(), articulo_id, ubicacion_id, num_remito.get())
        messagebox.showinfo("Información", "Ingreso registrado correctamente")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)
def agregar_categoria_gui():
    limpiar_pantalla()

    ttk.Label(root, text="Nombre de la categoría:").pack(pady=5)
    nombre = ttk.Entry(root)
    nombre.pack(pady=5)

    def guardar():
        agregar_categoria(nombre.get())
        messagebox.showinfo("Información", "Categoría agregada con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)
def agregar_estado_gui():
    limpiar_pantalla()

    ttk.Label(root, text="Nombre del estado:").pack(pady=5)
    nombre = ttk.Entry(root)
    nombre.pack(pady=5)

    def guardar():
        agregar_estado(nombre.get())
        messagebox.showinfo("Información", "Estado agregado con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=5)

if __name__ == '__main__':
    inicializar_bd()

    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("800x800")

    mostrar_menu()

    root.mainloop()
