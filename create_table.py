import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('deposito.db')
cursor = conn.cursor()

# Crear tabla para Marca
cursor.execute('''
CREATE TABLE IF NOT EXISTS marca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

# Crear tabla para Ubicacion
cursor.execute('''
CREATE TABLE IF NOT EXISTS ubicacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ubicacion TEXT NOT NULL
)
''')

# Crear tabla para Categoria
cursor.execute('''
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

# Crear tabla para Estado
cursor.execute('''
CREATE TABLE IF NOT EXISTS estado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

# Modificar tabla de Articulos para incluir referencias a las otras tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS articulos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    modelo TEXT NOT NULL,
    serial_number TEXT,
    cantidad INTEGER NOT NULL,
    ubicacion_id INTEGER,
    marca_id INTEGER,
    categoria_id INTEGER,
    estado_id INTEGER,
    FOREIGN KEY (marca_id) REFERENCES marca(id),
    FOREIGN KEY (ubicacion_id) REFERENCES ubicacion(id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(id),
    FOREIGN KEY (estado_id) REFERENCES estado(id)
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
