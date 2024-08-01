# data_layer.py
import sqlite3
from tkinter import messagebox

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
        CREATE TABLE IF NOT EXISTS egresos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATE NOT NULL,
            articulo_id INTEGER,
            cantidad INTEGER NOT NULL,
            destino TEXT,
            FOREIGN KEY (articulo_id) REFERENCES articulo(id)
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

url_db = 'deposito.db'
def obtener_conexion():
    return sqlite3.connect(url_db)

def listar_categorias():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categoria')
    categorias = cursor.fetchall()
    conn.close()
    return categorias
def guardar_categoria(nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categoria (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()

def listar_estados():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estado')
    estados = cursor.fetchall()
    conn.close()
    return estados
def guardar_estado(nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estado (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()

def listar_marcas():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM marca')
    marcas = cursor.fetchall()
    conn.close()
    return marcas
def guardar_marca(nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO marca (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()

def listar_articulos():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''
            SELECT 
                a.id, 
                a.nombre, 
                m.nombre AS marca, 
                a.modelo, 
                a.serial_number 
            FROM 
                articulos a 
            JOIN 
                marca m ON a.marca_id = m.id
        ''')
    articulos = cursor.fetchall()
    conn.close()
    return articulos

def guardar_articulo(nombre, modelo, serial_number, marca_id, categoria_id, estado_id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO articulos (nombre, modelo, serial_number, marca_id, categoria_id, estado_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, modelo, serial_number, marca_id, categoria_id, estado_id))
    conn.commit()
    conn.close()
def guardar_egreso(fecha, articulo_id, cantidad, destino):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO egresos (fecha, cantidad, articulo_id, destino) VALUES (?, ?, ?, ?)",
                       (fecha, articulo_id, cantidad, destino))
        cursor.execute("UPDATE inventario SET cantidad = cantidad - ? WHERE articulo_id = ?",
                       (cantidad, articulo_id))
        cursor.execute("COMMIT")
        conn.commit()
    except Exception as e:
        cursor.execute("ROLLBACK")
        messagebox.showerror("Error", f"Ocurrió un error al registrar el egreso: {e}")
    finally:
        conn.close()
def guardar_ingreso(fecha, cantidad, articulo_id, ubicacion_id, num_remito):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION")

        # Insertar el registro en la tabla de ingresos
        cursor.execute(
            "INSERT INTO ingresos (fecha, cantidad, articulo_id, ubicacion_id, remito) VALUES (?, ?, ?, ?, ?)",
            (fecha, cantidad, articulo_id, ubicacion_id, num_remito))

        # Verificar si el articulo_id y ubicacion_id existen en inventario
        cursor.execute("SELECT COUNT(*) FROM inventario WHERE articulo_id = ? AND ubicacion_id = ?",
                       (articulo_id, ubicacion_id))
        exists = cursor.fetchone()[0]

        if exists:
            # Actualizar el inventario si el registro ya existe
            cursor.execute("UPDATE inventario SET cantidad = cantidad + ? WHERE articulo_id = ? AND ubicacion_id = ?",
                           (cantidad, articulo_id, ubicacion_id))
        else:
            # Insertar un nuevo registro en el inventario si no existe
            cursor.execute("INSERT INTO inventario (articulo_id, ubicacion_id, cantidad) VALUES (?, ?, ?)",
                           (articulo_id, ubicacion_id, cantidad))

        cursor.execute("COMMIT")
        conn.commit()
    except Exception as e:
        cursor.execute("ROLLBACK")
        messagebox.showerror("Error", f"Ocurrió un error al registrar el ingreso: {e}")
    finally:
        conn.close()
def listar_ubicaciones():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ubicacion')
    ubicaciones = cursor.fetchall()
    conn.close()
    return ubicaciones
def listar_inventario(marca="", categoria="", modelo="", numero_serie=""):
    conn = obtener_conexion()
    cursor = conn.cursor()
    query = '''
        SELECT 
            i.id, 
            a.nombre, 
            m.nombre AS marca,
            c.nombre AS categoria,
            a.modelo, 
            a.serial_number, 
            i.cantidad, 
            u.nombre 
        FROM 
            inventario i 
        JOIN 
            articulos a ON i.articulo_id = a.id 
        JOIN 
            ubicacion u ON i.ubicacion_id = u.id
        JOIN 
            marca m ON a.marca_id = m.id
        JOIN 
            categoria c ON a.categoria_id = c.id
        WHERE 
            (? = '' OR m.nombre LIKE ?)
            AND (? = '' OR c.nombre LIKE ?)
            AND (? = '' OR a.modelo LIKE ?)
            AND (? = '' OR a.serial_number LIKE ?)
    '''
    cursor.execute(query, (marca, f"%{marca}%", categoria, f"%{categoria}%", modelo, f"%{modelo}%", numero_serie, f"%{numero_serie}%"))
    inventarios = cursor.fetchall()
    conn.close()
    return inventarios
