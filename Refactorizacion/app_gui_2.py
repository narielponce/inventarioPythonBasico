# app_gui_2.py
import tkinter as tk
from tkinter import ttk
import pandas as pd
from business_layer import *

def limpiar_pantalla():
    for widget in root.winfo_children():
        widget.destroy()
# MENU PRINCIPAL
    style = ttk.Style()
    style.configure('TButton', font=('Century Gothic', 10), background='grey', foreground='black')
    style.configure('TLabel', font=('Century Gothic', 9), background='grey')
    style.configure('TFrame', background='grey')
    style.configure('Treeview', background='lightgrey', foreground='black', fieldbackground='lightgrey')
    style.configure('Treeview.Heading', background='lightgrey', foreground='black')
    style.configure('TCombobox', font=('Century Gothic', 10), background='lightgrey', fieldbackground='lightgrey',
                    foreground='black')
def mostrar_menu():
    limpiar_pantalla()

    tit = ttk.Label(root, text="Gestión de Inventario Operaciones ITP - CIC", font=("Century Gothic", 16))
    tit.pack(pady=10)

    tit1 = ttk.Label(root, text="Maestro de artículos", font=("Century Gothic", 12))
    tit1.pack(pady=2)

    ttk.Button(root, text="Listado Maestro de artículos", command=listar_articulos_gui).pack(pady=2)
    ttk.Button(root, text="Alta nuevo artículo", command=agregar_articulo_gui).pack(pady=2)

    # Crear un widget Canvas
    canvas = tk.Canvas(root, width=450, height=2, bg='grey')
    canvas.pack(pady=2)

    tit2 = ttk.Label(root, text="Operaciones", font=("Century Gothic", 12))
    tit2.pack(pady=2)

    ttk.Button(root, text="Retiro de material", command=agregar_egreso_material_gui, style='Custom.TButton').pack(pady=2)
    ttk.Button(root, text="Ingreso de material", command=agregar_ingreso_material_gui, style='Custom.TButton').pack(pady=2)
    ttk.Button(root, text="Visualización de inventario", command=listar_inventario_gui, style='Custom.TButton').pack(pady=2)

    canvas = tk.Canvas(root, width=450, height=2, bg='grey')
    canvas.pack(pady=2)

    tit3 = ttk.Label(root, text="Tablas auxiliares", font=("Century Gothic", 12))
    tit3.pack(pady=2)

    ttk.Button(root, text="Agregar marca", command=agregar_marca_gui, style='Custom.TButton').pack(pady=2)
    ttk.Button(root, text="Listar marcas", command=listar_marcas_gui, style='Custom.TButton').pack(pady=2)

    ttk.Button(root, text="Agregar categoría", command=agregar_categoria_gui, style='Custom.TButton').pack(pady=2)
    ttk.Button(root, text="Listar categorías", command=listar_categorias_gui, style='Custom.TButton').pack(pady=2)

    ttk.Button(root, text="Agregar estado", command=agregar_estado_gui, style='Custom.TButton').pack(pady=2)
    ttk.Button(root, text="Listar estados", command=listar_estados_gui, style='Custom.TButton').pack(pady=2)

    canvas = tk.Canvas(root, width=450, height=2, bg='grey')
    canvas.pack(pady=2)

    tit2 = ttk.Label(root, text="Salir del sistema", font=("Century Gothic", 12))
    tit2.pack(pady=2)

    ttk.Button(root, text="Salir", command=root.quit, style='Custom.TButton').pack(pady=2)

def agregar_categoria_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Registro nueva categoría", font=("Century Gothic", 14))
    tit.pack(pady=10)

    ttk.Label(root, text="Nombre de la categoría:", font=('Century Gothic', 10)).pack(pady=2)
    nombre = ttk.Entry(root)
    nombre.pack(pady=2)

    def guardar():
        agregar_categoria(nombre.get())
        messagebox.showinfo("Información", "Categoría agregada con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar, style='Custom.TButton').pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu, style='Custom.TButton').pack(pady=2)
def listar_categorias_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Listado categorías", font=("Century Gothic", 14))
    tit.pack(pady=10)

    # Crear un frame para el Treeview y la scrollbar
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True, pady=20)

    # Crear el Treeview
    tree = ttk.Treeview(frame, columns=("ID", "Nombre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)

    # Crear el scrollbar vertical
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Empaquetar el Treeview y el scrollbar
    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')

    # Asegurarse de que el frame se expanda con el tamaño de la ventana
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Configurar el estilo de la fuente para las filas
    tree.tag_configure('fontstyle', font=('Century Gothic', 10))

    # Agregar las categorías al Treeview
    for categoria in listar_categorias():
        tree.insert("", tk.END, values=categoria, tags=('fontstyle',))

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)

def agregar_estado_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Registro nuevo estado", font=("Century Gothic", 14))
    tit.pack(pady=10)

    ttk.Label(root, text="Nombre del estado:").pack(pady=2)
    nombre = ttk.Entry(root)
    nombre.pack(pady=2)

    def guardar():
        agregar_estado(nombre.get())
        messagebox.showinfo("Información", "Estado agregado con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=2)
def listar_estados_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Listado estados", font=("Century Gothic", 14))
    tit.pack(pady=10)

    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("ID", "Nombre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)

    # Configurar el estilo de la fuente para las filas
    tree.tag_configure('fontstyle', font=('Century Gothic', 10))

    # Agregar los estados al Treeview
    for estado in listar_estados():
        tree.insert("", tk.END, values=estado, tags=('fontstyle',))

    tree.pack(pady=10)

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)

def listar_articulos_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Maestro de artículos", font=("Century Gothic", 14))
    tit.pack(pady=10)

    # Crear un frame para el Treeview y la scrollbar
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True, pady=20)

    # Crear el Treeview
    tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Modelo", "N° Serie", "Marca", "Categoría", "Estado"),
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

    # Crear el scrollbar vertical
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Empaquetar el Treeview y el scrollbar
    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')

    # Asegurarse de que el frame se expanda con el tamaño de la ventana
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Configurar el estilo de la fuente para las filas
    tree.tag_configure('fontstyle', font=('Century Gothic', 10))

    # Agregar los artículos al Treeview
    for articulo in listar_articulos():
        tree.insert("", tk.END, values=articulo, tags=('fontstyle',))

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)
def agregar_articulo_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Registro nuevo artículo", font=("Century Gothic", 14))
    tit.pack(pady=10)

    ttk.Label(root, text="Nombre del artículo:").pack(pady=2)
    nombre = ttk.Entry(root)
    nombre.pack(pady=2)

    ttk.Label(root, text="Modelo:").pack(pady=2)
    modelo = ttk.Entry(root)
    modelo.pack(pady=2)

    ttk.Label(root, text="Número de serie:").pack(pady=2)
    serial_number = ttk.Entry(root)
    serial_number.pack(pady=2)

    marcas = obtener_marcas()
    categorias = obtener_categorias()
    estados = obtener_estados()

    ttk.Label(root, text="Marca:").pack(pady=2)
    marca_cb = ttk.Combobox(root, values=[f"{marca[1]} (ID: {marca[0]})" for marca in marcas])
    marca_cb.pack(pady=2)

    ttk.Label(root, text="Categoría:").pack(pady=2)
    categoria_cb = ttk.Combobox(root, values=[f"{categoria[1]} (ID: {categoria[0]})" for categoria in categorias])
    categoria_cb.pack(pady=2)

    ttk.Label(root, text="Estado:").pack(pady=2)
    estado_cb = ttk.Combobox(root, values=[f"{estado[1]} (ID: {estado[0]})" for estado in estados])
    estado_cb.pack(pady=2)

    def guardar():
        marca_id = int(marca_cb.get().split("ID: ")[1][:-1])
        categoria_id = int(categoria_cb.get().split("ID: ")[1][:-1])
        estado_id = int(estado_cb.get().split("ID: ")[1][:-1])

        agregar_articulo(nombre.get(), modelo.get(), serial_number.get(), marca_id, categoria_id, estado_id)
        messagebox.showinfo("Información", "Artículo agregado con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=2)

def listar_marcas_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Listado de marcas", font=("Century Gothic", 14))
    tit.pack(pady=10)

    # Crear un frame para el Treeview y la scrollbar
    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True, pady=20)

    # Crear el Treeview
    tree = ttk.Treeview(frame, columns=("ID", "Nombre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Configurar el tamaño de las columnas
    tree.column("ID", width=30, anchor=tk.CENTER)
    tree.column("Nombre", width=120, anchor=tk.W)

    # Crear el scrollbar vertical
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Empaquetar el Treeview y el scrollbar
    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')

    # Asegurarse de que el frame se expanda con el tamaño de la ventana
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Configurar el estilo de la fuente para las filas
    tree.tag_configure('fontstyle', font=('Century Gothic', 10))

    # Agregar las marcas al Treeview
    for marca in listar_marcas():
        tree.insert("", tk.END, values=marca, tags=('fontstyle',))

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)
def agregar_marca_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Registro nueva marca", font=("Century Gothic", 14))
    tit.pack(pady=10)

    ttk.Label(root, text="Nombre de la marca:").pack(pady=2)
    nombre = ttk.Entry(root)
    nombre.pack(pady=2)

    def guardar():
        agregar_marca(nombre.get())
        messagebox.showinfo("Información", "Marca agregada con éxito")
        mostrar_menu()

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=2)

def listar_inventario_gui():
    limpiar_pantalla()

    categorias = obtener_categorias()
    marcas = obtener_marcas()

    categorias_nombres = [categoria[1] for categoria in categorias]
    marcas_nombres = [marca[1] for marca in marcas]

    filter_frame = ttk.Frame(root)
    filter_frame.pack(fill='x', pady=10)

    ttk.Label(filter_frame, text="Marca:").grid(row=0, column=0, padx=5)
    marca_combobox = ttk.Combobox(filter_frame, values=marcas_nombres)
    marca_combobox.grid(row=0, column=1, padx=5)

    ttk.Label(filter_frame, text="Categoría:").grid(row=0, column=2, padx=5)
    categoria_combobox = ttk.Combobox(filter_frame, values=categorias_nombres)
    categoria_combobox.grid(row=0, column=3, padx=5)

    ttk.Label(filter_frame, text="Modelo:").grid(row=0, column=4, padx=5)
    modelo_entry = ttk.Entry(filter_frame)
    modelo_entry.grid(row=0, column=5, padx=5)

    ttk.Label(filter_frame, text="N° Serie:").grid(row=0, column=6, padx=5)
    serie_entry = ttk.Entry(filter_frame)
    serie_entry.grid(row=0, column=7, padx=5)

    def aplicar_filtro():
        marca = marca_combobox.get()
        categoria = categoria_combobox.get()
        modelo = modelo_entry.get()
        numero_serie = serie_entry.get()
        actualizar_treeview(marca, categoria, modelo, numero_serie)

    def limpiar_filtros():
        marca_combobox.set('')
        categoria_combobox.set('')
        modelo_entry.delete(0, tk.END)
        serie_entry.delete(0, tk.END)
        actualizar_treeview("", "", "", "")

    def exportar_excel():
        marca = marca_combobox.get()
        categoria = categoria_combobox.get()
        modelo = modelo_entry.get()
        numero_serie = serie_entry.get()
        inventarios = obtener_inventario_filtrado(marca, categoria, modelo, numero_serie)
        df = pd.DataFrame(inventarios,
                          columns=["ID", "Artículo", "Marca", "Categoría", "Modelo", "N° Serie", "Cantidad",
                                   "Ubicación"])
        df.to_excel("inventario.xlsx", index=False)
        messagebox.showinfo("Exportar a Excel", "El inventario se ha exportado exitosamente a 'inventario.xlsx'.")

    ttk.Button(filter_frame, text="Aplicar Filtro", command=aplicar_filtro).grid(row=0, column=8, padx=5)
    ttk.Button(filter_frame, text="Limpiar Filtros", command=limpiar_filtros).grid(row=0, column=9, padx=5)
    ttk.Button(filter_frame, text="Exportar a Excel", command=exportar_excel).grid(row=0, column=10, padx=5)

    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True, pady=20)

    tree = ttk.Treeview(frame,
                        columns=("ID", "Artículo", "Marca", "Categoría", "Modelo", "N° Serie", "Cantidad", "Ubicación"),
                        show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Artículo", text="Artículo")
    tree.heading("Marca", text="Marca")
    tree.heading("Categoría", text="Categoría")
    tree.heading("Modelo", text="Modelo")
    tree.heading("N° Serie", text="N° Serie")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Ubicación", text="Ubicación")

    tree.column("ID", width=20, anchor=tk.CENTER)
    tree.column("Artículo", width=200, anchor=tk.W)
    tree.column("Marca", width=60, anchor=tk.W)
    tree.column("Categoría", width=100, anchor=tk.W)
    tree.column("Modelo", width=150, anchor=tk.W)
    tree.column("N° Serie", width=150, anchor=tk.W)
    tree.column("Cantidad", width=40, anchor=tk.W)
    tree.column("Ubicación", width=150, anchor=tk.W)

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    def actualizar_treeview(marca, categoria, modelo, numero_serie):
        for row in tree.get_children():
            tree.delete(row)

        for inventario in obtener_inventario_filtrado(marca, categoria, modelo, numero_serie):
            tree.insert("", tk.END, values=inventario)

    actualizar_treeview("", "", "", "")

    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=20)
def agregar_egreso_material_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Registro nueva salida de material", font=("Century Gothic", 14))
    tit.pack(pady=10)

    articulos = obtener_articulos()

    # Crear etiqueta y campo de entrada para la fecha
    ttk.Label(root, text="Fecha egreso material (DD/MM/YYYY):").pack(pady=10)
    fecha_entry = ttk.Entry(root)
    fecha_entry.pack(pady=2)

    #ttk.Label(root, text="Artículo:").pack(pady=2)
    #articulo_cb = ttk.Combobox(root, width=60, values=[
    #    f"{articulo[1]} - {articulo[2]} - {articulo[3]} - SN: {articulo[4]}"
    #    for articulo in articulos])
    #articulo_cb.pack(pady=2)

    # Crear combobox de artículos con un valor oculto (artiulo_id)
    ttk.Label(root, text="Artículo:").pack(pady=2)
    articulo_cb = ttk.Combobox(root, width=60)
    articulo_cb.pack(pady=2)
    articulo_cb['values'] = [f"{articulo[1]} - {articulo[2]} - {articulo[3]} - SN: {articulo[4]}" for articulo in
                             articulos]
    articulo_ids = {f"{articulo[1]} - {articulo[2]} - {articulo[3]} - SN: {articulo[4]}": articulo[0] for articulo in
                    articulos}

    ttk.Label(root, text="Cantidad:").pack(pady=2)
    cantidad = ttk.Entry(root)
    cantidad.pack(pady=2)

    ttk.Label(root, text="Lugar destino:").pack(pady=2)
    destino = ttk.Entry(root)
    destino.pack(pady=2)

    def guardar():
        try:
            articulo_texto = articulo_cb.get()
            #articulo_id = int(articulo_texto.split("ID: ")[1].split(")")[0])
            articulo_id = articulo_ids.get(articulo_texto)

            if articulo_id is None:
                raise ValueError("ID no válido")

            agregar_egreso(fecha_entry.get(), articulo_id, cantidad.get(), destino.get())
            messagebox.showinfo("Información", "Egreso registrado correctamente")
            mostrar_menu()
        except IndexError:
            messagebox.showerror("Error", "Seleccione un artículo válido.")
        except ValueError:
            messagebox.showerror("Error", "El ID del artículo no es válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=2)
def agregar_ingreso_material_gui():
    limpiar_pantalla()
    tit = ttk.Label(root, text="Registro nuevo ingreso a depósito", font=("Century Gothic", 14))
    tit.pack(pady=10)

    articulos = obtener_articulos()
    ubicaciones = obtener_ubicaciones()

    # Crear etiqueta y campo de entrada para la fecha
    ttk.Label(root, text="Fecha ingreso material (DD/MM/YYYY):").pack(pady=10)
    fecha_entry = ttk.Entry(root)
    fecha_entry.pack(pady=2)

    ttk.Label(root, text="Cantidad:").pack(pady=2)
    cantidad = ttk.Entry(root)
    cantidad.pack(pady=2)

    #ttk.Label(root, text="Artículo:").pack(pady=2)
    #articulo_cb = ttk.Combobox(root, width=60, values=[
    #    f"{articulo[1]} - {articulo[2]} - {articulo[3]} - SN: {articulo[4]}"
    #    for articulo in articulos])
    #articulo_cb.pack(pady=2)

    # Crear combobox de artículos con un valor oculto (artiulo_id)
    ttk.Label(root, text="Artículo:").pack(pady=2)
    articulo_cb = ttk.Combobox(root, width=60)
    articulo_cb.pack(pady=2)
    articulo_cb['values'] = [f"{articulo[1]} - {articulo[2]} - {articulo[3]} - SN: {articulo[4]}" for articulo in
                             articulos]
    articulo_ids = {f"{articulo[1]} - {articulo[2]} - {articulo[3]} - SN: {articulo[4]}": articulo[0] for articulo in
                    articulos}

    #ttk.Label(root, text="Ubicación:").pack(pady=2)
    #ubicacion_cb = ttk.Combobox(root, values=[f"{ubicacion[1]} (ID: {ubicacion[0]})" for ubicacion in ubicaciones])
    #ubicacion_cb.pack(pady=2)

    # Crear combobox de ubicaciones con un valor oculto (ubicacion_id)
    ttk.Label(root, text="Ubicación:").pack(pady=2)
    ubicacion_cb = ttk.Combobox(root)
    ubicacion_cb.pack(pady=2)
    ubicacion_cb['values'] = [f"{ubicacion[1]} (ID: {ubicacion[0]})" for ubicacion in ubicaciones]
    ubicacion_ids = {f"{ubicacion[1]} (ID: {ubicacion[0]})": ubicacion[0] for ubicacion in ubicaciones}

    ttk.Label(root, text="N° Remito / Proveedor:").pack(pady=2)
    num_remito = ttk.Entry(root)
    num_remito.pack(pady=2)

    def guardar():
        try:
            articulo_texto = articulo_cb.get()
            ubicacion_texto = ubicacion_cb.get()

            #articulo_id = int(articulo_texto.split("ID: ")[1].split(")")[0])
            articulo_id = articulo_ids.get(articulo_texto)
            #ubicacion_id = int(ubicacion_texto.split("ID: ")[1].split(")")[0])
            ubicacion_id = ubicacion_ids.get(ubicacion_texto)

            if articulo_id is None or ubicacion_id is None:
                raise ValueError("ID no válido")

            agregar_ingreso(fecha_entry.get(), cantidad.get(), articulo_id, ubicacion_id, num_remito.get())
            messagebox.showinfo("Información", "Ingreso registrado correctamente")
            mostrar_menu()
        except IndexError:
            messagebox.showerror("Error", "Seleccione un artículo y una ubicación válidos.")
        except ValueError:
            messagebox.showerror("Error", "El ID del artículo o la ubicación no es válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    ttk.Button(root, text="Guardar", command=guardar).pack(pady=20)
    ttk.Button(root, text="Volver", command=mostrar_menu).pack(pady=2)

#MAIN

if __name__ == '__main__':
    inicializar_bd()

    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("1200x600")
    root.resizable(False, False)

    # Cambiar el color de fondo de la ventana principal
    root.configure(bg='grey')

    mostrar_menu()

    root.mainloop()