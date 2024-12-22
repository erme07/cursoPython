
import sqlite3 # importamos modulo

from utilidades import *
from menus import *

#::::::::::::::: base de datos ::::::::::::::::

def conectar():
    """Función que conecta a la base de datos y la crea si no existe"""
    conn = sqlite3.connect('inventario.db')
    return conn

def crear_tabla(): #creo la tabla libros en la base de datos, solo si no existe
    """Función que crea la tabla libros en la base de datos"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )    
    """)

def base_datos_vacia(conexion):
    """Función que verifica si la base de datos está vacía"""
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM libros")
    vacia = cursor.fetchone()
    return vacia[0] == 0

def cargar_datos_iniciales(datos): #carga los libros de relleno en la base de datos, solo si está vacia
    """Función que carga los datos iniciales en la base de datos"""
    conexion = conectar()
    cursor = conexion.cursor()
    if base_datos_vacia(conexion):
        cursor.executemany("""
            INSERT INTO libros (titulo, autor, categoria, precio, stock)
            VALUES (?, ?, ?, ?, ?)
        """, datos)
        conexion.commit()
    conexion.close()


#::::::::::::::: funciones principales ::::::::::::::::

def ingresar_libro():
    """Función que recibe los datos del libro a ingresar"""
    limpiar_consola()
    titulo = input("\n🔤 Ingrese el titulo: ")
    limpiar_consola()
    autor = input("\n🔤 Ingrese el autor: ").title()
    limpiar_consola()
    categoria = menu_categorias() #solo hay 5 categorias, se elijen mediante un menu
    precio = establecer_precio()
    limpiar_consola()
    stock = establecer_stock()
    limpiar_consola()
    libro = (titulo,autor,categoria,precio,stock)
    while True:
        mostrar_libro(libro) #muestra los datos ingresados
        accion = menu_confirmacion("confirmacion") #pregunta que desa hacer con los datos ingresados
        if(accion=="confirmar"):
            guardar_en_inventario(libro) #los datos ingresados se guardan en la base de datos
            break #si elije guardar los datos, se sale del bucle
        elif(accion=="modificar"): #permite modificar los datos ingresados
            libro = modificar_datos(libro) 
        else: #se descartan los datos ingresados
            print("\nIngreso de libro cancelado.")
            input("\nPresione ENTER ⤵️  para continuar... ")
            break

def mostrar_inventario():
    """Función que muestra todo el inventario"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    limpiar_consola()
    print(f"\n{'INVENTARIO DE LIBROS 📖':^117}\n")
    imprimir_marco_inventario(len(libros)) #imprime el marco visual de la tabla
    num_libro=0
    while num_libro<len(libros): #muestr0 los datos de los libros
        color = nivel_stock(libros[num_libro][5]) #segun el nivel de stock, se asigna un color
        print(f"\033[2C{libros[num_libro][0]:<3} \033[1C {libros[num_libro][1]:<45} \033[1C {libros[num_libro][2]:<25} \033[1C {libros[num_libro][3]:<15} \033[1C ${libros[num_libro][4]:<9} \033[1C {color}{libros[num_libro][5]:<5}{Style.RESET_ALL}")
        num_libro+=1
    print(f"\033[1B", end='')
    print(f"\033[75C{'Stock bajo:'}{Fore.RED} \u2588\u2588 {Style.RESET_ALL} {'Stock medio:'}{Fore.YELLOW} \u2588\u2588 {Style.RESET_ALL} {'Stock alto:'}{Fore.GREEN} \u2588\u2588 {Style.RESET_ALL}")
    conexion.close()

def actualizar_libro():
    """Función que actualiza datos de un libro del inventario"""
    mostrar_inventario()
    conexion = conectar()
    cursor = conexion.cursor()
    print()
    id_libro = establecer_id()
    if busqueda_base_datos(conexion,'id',id_libro): #verifica si el libro existe buscando en la base de datos
        cursor.execute("SELECT * FROM libros WHERE id = ?", (id_libro,))
        libro = cursor.fetchone()
        libro_sin_id = libro[1:] # Elimino el campo ID del libro para que no sea modificable
        libro_sin_id = modificar_datos(libro_sin_id)
        while True:
            mostrar_libro(libro_sin_id)
            accion = menu_confirmacion("actualizacion") #pregunta que desa hacer con los datos modificados
            if(accion=="confirmar"): #sale del bucle si elige guardar los cambios
                break
            elif(accion=="modificar"): #permite continuar modificando los datos
                libro_sin_id = modificar_datos(libro_sin_id)
            else: #se descartan los cambios realizados
                print("\nActualizacion de libro cancelada.")
                input("\nPresione ENTER ⤵️  para continuar... ")
                conexion.close()
                return
        # Actualizo los datos del libro en la base de datos
        campos_sql = 'titulo = ?, autor = ?, categoria = ?, precio = ?, stock = ?'
        cursor.execute(f"UPDATE libros SET {campos_sql} WHERE id = ?", (*libro_sin_id, id_libro))
        conexion.commit()
        print()
        barra_progreso("ACTUALIZANDO")
        print("\nLibro actualizado exitosamente.")
    else:
        print(f"\nEl libro de ID {id_libro} no existe.")
    input("\nPresione ENTER ⤵️  para continuar... ")
    conexion.close() 

def remover_libro():
    """Función que remueve un libro del inventario"""
    mostrar_inventario()
    conexion = conectar()
    cursor = conexion.cursor()
    print()
    id_libro = establecer_id()
    if busqueda_base_datos(conexion,'id',id_libro): #verifica si el libro existe buscando en la base de datos
        cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
        conexion.commit() #elimina el libro de la base de datos
        print()
        barra_progreso("ELIMINANDO")
        print("\nLibro eliminado exitosamente.")
    else:
        print(f"\nEl libro de ID {id_libro} no existe.")
    input("\nPresione ENTER ⤵️  para continuar... ")
    conexion.close() 

def buscar_libro():
    conexion = conectar()
    limpiar_consola()
    criterio = menu_busqueda() #se elije el criterio de busqueda mediante un menu
    if criterio == "id": #si el criterio es el ID, se solicita el ID
        valor = establecer_id()
    elif criterio == "titulo" or criterio == "autor": #si el criterio es titulo o autor, se solicita el valor
        valor = input(f"🔤 Ingrese el {criterio} del libro a buscar: ")
    else:
        valor = menu_categorias() #si el criterio es categoria, se elije mediante un menu
    libro = busqueda_base_datos(conexion,criterio,valor) #se realiza la busqueda en la base de datos
    barra_progreso("BUSCANDO")
    limpiar_consola()
    if libro:
        mostrar_resultados_busqueda(libro) #si se encuentra libros, se muestran los datos
        print()
    else:
        print(f"No se encontraron libros con {criterio} igual a \"{valor}\".")
    input("\nPresione ENTER ⤵️  para continuar... ")
    conexion.close()

def bajo_stock(): #se consideran con bajo stock a los libros con menos de 10 ejemplares disponibles
    """Función que genera un reporte de libros con bajo stock"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE stock < ?", (10,)) #busca los libros con stock menor a 10
    libros = cursor.fetchall()
    limpiar_consola()
    barra_progreso("BUSCANDO")
    limpiar_consola()
    if libros:
        mostrar_libros_bajo_stock(libros) #si hay libros con bajo stock, se muestran los datos
        print()
    else:
        print("No hay libros con bajo stock.")
    input("\nPresione ENTER ⤵️  para continuar... ")
    conexion.close()


#::::::::::::::: funciones auxiliares ::::::::::::::::

def modificar_datos(libro): #modifica los datos de un libro ingresado por el usuario o los de un libro ya existente en la base de datos
    """Función que modifica los datos de un libro"""
    libro = list(libro)
    limpiar_consola()
    mostrar_libro(libro) #muestra los datos del libro
    campo = menu_edicion() #se elije el campo a modificar mediante un menu
    limpiar_consola()
    if campo == "titulo": #se modifica el titulo
        print(f"\nTITULO ACTUAL: {Fore.LIGHTGREEN_EX}{libro[0]}\n")
        libro[0] = input("🔤 Ingrese el nuevo titulo: ")
    elif campo == "autor": #se modifica el autor
        print(f"\nAUTOR ACTUAL: {Fore.LIGHTGREEN_EX}{libro[1]}\n")
        libro[1] = input("🔤 Ingrese el nuevo autor: ") 
    elif campo == "categoria": #se modifica la categoria
        print(f"\nCATEGORIA ACTUAL: {Fore.LIGHTGREEN_EX}{libro[2]}\n")
        libro[2] = menu_categorias()
    elif campo == "precio": #se modifica el precio
        print(f"\nPRECIO ACTUAL: {Fore.LIGHTGREEN_EX}{'$'+str(libro[3])}\n")
        libro[3] = establecer_precio()
    elif campo == "stock": #se modifica el stock
        print(f"\nSTOCK ACTUAL: {Fore.LIGHTGREEN_EX}{libro[4]}\n")
        libro[4] = establecer_stock()
    limpiar_consola()
    return tuple(libro) #retorna una tupla con los datos modificados

def guardar_en_inventario(libro):
    """Función que guarda el libro en la base de datos"""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
                INSERT INTO libros (titulo, autor, categoria, precio, stock) 
                VALUES (?, ?, ?, ?, ?)
            """, libro)
    conexion.commit()
    conexion.close()
    print()
    barra_progreso("GUARDANDO")
    print("\nLibro guardado exitosamente.")
    input("\nPresione ENTER ⤵️  para continuar... ")


def busqueda_base_datos(conexion,campo,valor):
    """Función que verifica si el libro con el campo indicado existe en la base de datos"""
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM libros WHERE LOWER({campo}) = LOWER(?)", (valor,))
    libro = cursor.fetchall()
    return libro if libro else False #se retorna el/los libros con el campo especificado si existen, sino se retorna Falso



#::::::::::::::: manejo/validacion de datos ::::::::::::::::

def establecer_stock():
    """Función que solicita y valida el stock de un libro"""
    stock = input("\n🔢 Ingrese la cantidad: ")
    while True:
        if stock.isdigit() or (stock.startswith('-') and stock[1:].isdigit()):
            num = int(stock)
            if(num > 0):
                break
        print("\nError: La cantidad debe ser un numero entero mayor a cero.")
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
        stock = input("\n🔢 Ingrese la cantidad: ")
    return stock

def establecer_precio():
    """Función que solicita y valida el precio de un libro"""
    precio = input("\n💵 Ingrese el precio: $")
    while True:
        if es_decimal(precio):
            num = float(precio)
            if(num > 0):
                break
        print("\nError: La cantidad debe ser un numero mayor a cero.")
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
        precio = input("\n💵 Ingrese el precio: $")
    return precio

def establecer_id():
    """Función que solicita y valida el ID de un libro"""
    while True:
        id_libro = input("Ingrese el ID del libro: ")
        if id_libro.isdigit():
            return int(id_libro)
        print("Error: Debe ingresar un número entero positivo.")