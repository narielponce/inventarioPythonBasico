# business_layer.py
from data_layer import *

def obtener_categorias():
    return listar_categorias()
def agregar_categoria(nombre):
    return guardar_categoria(nombre)

def obtener_estados():
    return listar_estados()
def agregar_estado(nombre):
    guardar_estado(nombre)
    return

def obtener_marcas():
    return listar_marcas()
def agregar_marca(nombre):
    return  guardar_marca(nombre)

def obtener_articulos():
    return listar_articulos()
def agregar_articulo(nombre, modelo, serial_number, marca_id, categoria_id, estado_id):
    return guardar_articulo(nombre, modelo, serial_number, marca_id, categoria_id, estado_id)
def agregar_egreso(fecha, articulo_id, cantidad, destino):
    return guardar_egreso(fecha, articulo_id, cantidad, destino)
def agregar_ingreso(fecha, cantidad, articulo_id, ubicacion_id, num_remito):
    return guardar_ingreso(fecha, cantidad, articulo_id, ubicacion_id, num_remito)
def obtener_ubicaciones():
    return listar_ubicaciones()
def obtener_inventario_filtrado(marca, categoria, modelo, numero_serie):
    return listar_inventario(marca, categoria, modelo, numero_serie)
