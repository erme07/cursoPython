#Inventario de libros

import os
import sqlite3 # importamos modulo
import time
from colorama import Fore, Style, Back, init
init(autoreset=True)



def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

datos = [
  ("Fuego y Sangre","George R.R. Martin","Fantasia",25500,30),
  ("El Hobbit","J.R.R. Tolkien","Fantasia",36300,25),
  ("Orgullo y Prejuicio","Jane Austen","Romance",21100,10),
  ("Harry Potter y la Piedra Filosofal","J.K. Rowling","Fantasia",63700,15),
  ("Misery","Stephen King","Terror",27700,10),
  ("Los Crimenes de la Calle Morgue","Edgar Allan Poe","Policial",10450,13),
  ("La Guerra de los Mundos","H.G. Wells","Ciencia Ficcion",5400,24)
]

#print('SQLite version:',sqlite3.sqlite_version) # vemos version

def conectar():
    conn = sqlite3.connect('inventario.db')
    return conn

#conn = conectar()
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS libros (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   titulo TEXT NOT NULL,
#   autor TEXT NOT NULL,
#   categoria TEXT NOT NULL,
#   precio REAL NOT NULL,
#   stock INTEGER NOT NULL
# )    
# """)

# Verificar si ya existen datos en la tabla
# cursor.execute("SELECT COUNT(*) FROM libros")
# vacia = cursor.fetchone()

# if vacia[0] == 0:  # Si la tabla está vacía
#   cursor.executemany("""
#   INSERT INTO libros (titulo, autor, categoria, precio, stock)
#   VALUES (?, ?, ?, ?, ?)
#   """, datos)

# conn.commit()

# cursor.execute("SELECT * FROM libros")
# filas = cursor.fetchall()

opcion = None
salir = 7


#::::::::::::::: Formateado de menus ::::::::::::::::

def imprimir_marco(filas):
    """Imprime un marco visual que contiene los distintos menus."""
    print("\u2554" + "\u2550" * 47 + "\u2557")
    print("\u2551" + " " * 47 + "\u2551")
    print("\u2560" + "\u2550" * 47 + "\u2563")
    for _ in range(filas):
        print("\u2551" + " " * 47 + "\u2551")
    print("\u255A" + "\u2550" * 47 + "\u255D")
    print(f"\033[{filas+3}A", end='')

def imprimir_menu_principal():
    """Muestra el menú principal con una mejora visual."""
    imprimir_marco(11)
    print(f"\033[1C{Style.BRIGHT + 'MENÚ PRINCIPAL  🏠':^49}\n\n")
    print(f"\033[2C [{Fore.YELLOW + '1' + Style.RESET_ALL}] {'Ingresar un nuevo libro'}")
    print(f"\033[2C [{Fore.YELLOW + '2' + Style.RESET_ALL}] {'Mostrar inventario'}")
    print(f"\033[2C [{Fore.YELLOW + '3' + Style.RESET_ALL}] {'Actualizar libro'}")
    print(f"\033[2C [{Fore.YELLOW + '4' + Style.RESET_ALL}] {'Remover libro'}")
    print(f"\033[2C [{Fore.YELLOW + '5' + Style.RESET_ALL}] {'Buscar libro'}")
    print(f"\033[2C [{Fore.YELLOW + '6' + Style.RESET_ALL}] {'Reporte de bajo stock'}")
    print(f"\033[2C [{Fore.YELLOW + '7' + Style.RESET_ALL}] {Fore.RED +'Salir'+ Style.RESET_ALL}\n")
    print("\033[3C", end='')

def imprimir_menu_categorias():
    """Muestra el menú de seleccion de categoria."""
    imprimir_marco(9)
    print(f"\033[1C{Style.BRIGHT + 'CATEGORIAS':^49}\n\n")
    print(f"\033[2C [{Fore.YELLOW}{'1'}{Style.RESET_ALL}] {'Terror'}")
    print(f"\033[2C [{Fore.YELLOW}{'2'}{Style.RESET_ALL}] {'Ciencia Ficcion'}")
    print(f"\033[2C [{Fore.YELLOW}{'3'}{Style.RESET_ALL}] {'Romance'}")
    print(f"\033[2C [{Fore.YELLOW}{'4'}{Style.RESET_ALL}] {'Fantasia'}")
    print(f"\033[2C [{Fore.YELLOW}{'5'}{Style.RESET_ALL}] {'Policial'}\n")
    print("\033[3C", end='')

def imprimir_menu_confirmacion():
    """Muestra el menú de confirmacion de ingreso al inventario."""
    imprimir_marco(7)
    print(f"\033[1C{Style.BRIGHT + 'Añadir el libro al inventario?':^49}\n\n")
    print(f"\033[2C [{Fore.YELLOW}{'1'}{Style.RESET_ALL}] {'Añadir al inventario'}")
    print(f"\033[2C [{Fore.YELLOW}{'2'}{Style.RESET_ALL}] {'Modificar los datos'}")
    print(f"\033[2C [{Fore.YELLOW}{'3'}{Style.RESET_ALL}] {Fore.RED}{'Cancelar'}{Style.RESET_ALL}\n")
    print("\033[3C", end='')

def imprimir_menu_actualizacion():
    """Muestra el menú de actualizacion de libro."""
    imprimir_marco(7)
    print(f"\033[1C{Style.BRIGHT + 'Actualizacion de libro 🔄':^49}\n\n")
    print(f"\033[2C [{Fore.YELLOW}{'1'}{Style.RESET_ALL}] {'Guardar Cambios'}")
    print(f"\033[2C [{Fore.YELLOW}{'2'}{Style.RESET_ALL}] {'Modificar mas campos'}")
    print(f"\033[2C [{Fore.YELLOW}{'3'}{Style.RESET_ALL}] {Fore.RED}{'Cancelar cambios'}{Style.RESET_ALL}\n")
    print("\033[3C", end='')

def imprimir_menu_edicion():
    """Muestra el menú de seleccion de campo a editar."""
    imprimir_marco(9)
    print(f"\033[1C{Style.BRIGHT}{'CAMPOS EDITABLES  ✏️':^48}\n\n")
    print(f"\033[2C [{Fore.YELLOW}{'1'}{Style.RESET_ALL}] {'Titulo'}")
    print(f"\033[2C [{Fore.YELLOW}{'2'}{Style.RESET_ALL}] {'Autor'}")
    print(f"\033[2C [{Fore.YELLOW}{'3'}{Style.RESET_ALL}] {'Categoria'}")
    print(f"\033[2C [{Fore.YELLOW}{'4'}{Style.RESET_ALL}] {'Precio'}")
    print(f"\033[2C [{Fore.YELLOW}{'5'}{Style.RESET_ALL}] {'Stock'}\n")
    print("\033[3C", end='')


#::::::::::::::: logica de menus ::::::::::::::::

def menu_principal():
  opcion_min = 1
  opcion_max = 7
  while True:
    imprimir_menu_principal()
    opc = input("Seleccione una opcion: ")
    if opc.isdigit() or (opc.startswith('-') and opc[1:].isdigit()):
      opc = int(opc)
      if(opc >= opcion_min and opc <= opcion_max):
        break
    print(f"\n\"{opc}\" no es una opcion valida 🚫, intente nuevamente")
    input("\nPresione ENTER ⤵️   para continuar... ")
    limpiar_consola()
  return opc

def menu_categorias():
  categorias_validas = ["Terror", "Ciencia Ficcion", "Romance", "Fantasia", "Policial"]
  opcion_min = 1
  opcion_max = 5
  while True:
    imprimir_menu_categorias()
    opc = input("Seleccione la categoria: ")
    if opc.isdigit() or (opc.startswith('-') and opc[1:].isdigit()):
      opc = int(opc)
      if(opc >= opcion_min and opc <= opcion_max):
        break
    print(f"\n\"{opc}\" no es una opcion valida 🚫, intente nuevamente")
    input("\nPresione ENTER ⤵️   para continuar... ")
    limpiar_consola()
  limpiar_consola()
  return categorias_validas[opc-1]

def menu_confirmacion(menu_tipo):
  acciones = ("confirmar","modificar","cancelar")
  opcion_min = 1
  opcion_max = 3
  while True:
    if(menu_tipo == "actualizacion"):
      imprimir_menu_actualizacion()
    else:
      imprimir_menu_confirmacion()
    opc = input("Seleccione una opcion: ")
    if opc.isdigit() or (opc.startswith('-') and opc[1:].isdigit()):
      opc = int(opc)
      if(opc >= opcion_min and opc <= opcion_max):
        break
    print(f"\n\"{opc}\" no es una opcion valida 🚫, intente nuevamente")
    input("\nPresione ENTER ⤵️   para continuar... ")
    limpiar_consola()
  return acciones[opc-1]

def menu_edicion():
  opcion_min = 1
  opcion_max = 5
  while True:
    imprimir_menu_edicion()
    opc = input("Seleccione el campo a editar: ")
    if opc.isdigit() or (opc.startswith('-') and opc[1:].isdigit()):
      opc = int(opc)
      if(opc >= opcion_min and opc <= opcion_max):
        break
    print(f"\n\"{opc}\" no es una opcion valida 🚫, intente nuevamente")
    input("\nPresione ENTER ⤵️   para continuar... ")
    limpiar_consola()
  return opc


#::::::::::::::: manejo de datos ::::::::::::::::

def establecer_stock():
  stock = input("\n🔢 Ingrese la cantidad: ")
  while True:
    if stock.isdigit() or (stock.startswith('-') and stock[1:].isdigit()):
      num = int(stock)
      if(num > 0):
        break
    print("\nError: La cantidad debe ser un numero entero mayor a cero.")
    input("\nPresione ENTER ⤵️   para continuar... ")
    limpiar_consola()
    stock = input("\n🔢 Ingrese la cantidad: ")
  return stock

def establecer_precio():
  precio = input("\n💵 Ingrese el precio: $")
  while True:
    if es_decimal(precio):
      num = float(precio)
      if(num > 0):
        break
    print("\nError: La cantidad debe ser un numero mayor a cero.")
    input("\nPresione ENTER ⤵️   para continuar... ")
    limpiar_consola()
    precio = input("\n💵 Ingrese el precio: $")
  return precio

def establecer_id():
    """Función que solicita y valida el ID de un libro"""
    while True:
      id_libro = input("Ingrese el ID del libro a eliminar: ")
      if id_libro.isdigit():
          return int(id_libro)
      print("Error: Debe ingresar un número entero positivo.")







#::::::::::::::: visualizacion de datos ::::::::::::::::

def mostrar_libro(libro):
  print(f"\n{'DATOS DEL LIBRO 📖':^117}\n")
  print("\u2554" + "\u2550"*47 + "\u2566" + "\u2550"*27 + "\u2566" + "\u2550"*17 + "\u2566" + "\u2550"*12 + "\u2566" + "\u2550"*7 + "\u2557")
  print(f"\u2551 {Back.WHITE+Fore.BLACK}{'Titulo':^45}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Autor':^25}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Categoria':^15}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Precio':^10}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Stock':^5}{Style.RESET_ALL} \u2551")
  print("\u2560" + "\u2550"*47 + "\u256C" + "\u2550"*27 + "\u256C" + "\u2550"*17 + "\u256C" + "\u2550"*12 + "\u256C" + "\u2550"*7 + "\u2563")
  print(f"\u2551 {libro[0]:^45} \u2551 {libro[1]:^25} \u2551 {libro[2]:^15} \u2551 {'$'+str(libro[3]):^10} \u2551 {libro[4]:^5} \u2551")
  print("\u255A" + "\u2550"*47 + "\u2569" + "\u2550"*27 + "\u2569" + "\u2550"*17 + "\u2569" + "\u2550"*12 + "\u2569" + "\u2550"*7 + "\u255D")



#::::::::::::::: funciones principales ::::::::::::::::

def ingresar_libro():
  """Función que recibe los datos del libro a ingresar"""
  limpiar_consola()
  titulo = input("\n🔤 Ingrese el titulo: ")
  limpiar_consola()
  autor = input("\n🔤 Ingrese el autor: ").title()
  limpiar_consola()
  categoria = menu_categorias()
  precio = establecer_precio()
  limpiar_consola()
  stock = establecer_stock()
  limpiar_consola()
  libro = (titulo,autor,categoria,precio,stock)
  while True:
    mostrar_libro(libro)
    accion = menu_confirmacion("confirmacion")
    if(accion=="confirmar"):
      guardar_en_inventario(libro)
      break
    elif(accion=="modificar"):
      libro = modificar_datos(libro)
    else:
      print("\nIngreso de libro cancelado.")
      input("\nPresione ENTER ⤵️   para continuar... ")
      break

def mostrar_inventario():
  """Función que muestra todo el inventario"""
  libros = []
  conexion = conectar()
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM libros")
  libros = cursor.fetchall()
  limpiar_consola()
  print(f"\n{'INVENTARIO DE LIBROS 📖':^117}\n")
  print("\u2554" + "\u2550"*5 + "\u2566" + "\u2550"*47 + "\u2566" + "\u2550"*27 + "\u2566" + "\u2550"*17 + "\u2566" + "\u2550"*12 + "\u2566" + "\u2550"*7 + "\u2557")
  print(f"\u2551 {'ID':<3} \u2551 {'Titulo':<45} \u2551 {'Autor':<25} \u2551 {'Categoria':<15} \u2551 {'Precio':<10} \u2551 {'Stock':<5} \u2551")
  print("\u2560" + "\u2550"*5 + "\u256C" + "\u2550"*47 + "\u256C" + "\u2550"*27 + "\u256C" + "\u2550"*17 + "\u256C" + "\u2550"*12 + "\u256C" + "\u2550"*7 + "\u2563")
  num_libro=0
  while num_libro<len(libros):
    color = nivel_stock(libros[num_libro][5])
    print(
      f"\u2551 {libros[num_libro][0]:<3} \u2551 {libros[num_libro][1]:<45} \u2551 {libros[num_libro][2]:<25} \u2551 {libros[num_libro][3]:<15} \u2551 ${libros[num_libro][4]:<9} \u2551 "
      f"{color}{libros[num_libro][5]:<5}{Style.RESET_ALL} \u2551"
    )
    num_libro+=1
  print("\u255A" + "\u2550"*5 + "\u2569" + "\u2550"*47 + "\u2569" + "\u2550"*27 + "\u2569" + "\u2550"*17 + "\u2569" + "\u2550"*12 + "\u2569" + "\u2550"*7 + "\u255D")
  print(f"\033[75C{'Stock bajo:'}{Fore.RED} \u2588\u2588 {Style.RESET_ALL} {'Stock medio:'}{Fore.YELLOW} \u2588\u2588 {Style.RESET_ALL} {'Stock alto:'}{Fore.GREEN} \u2588\u2588 {Style.RESET_ALL}")
  
  # print(f"")
  conexion.close()

def actualizar_libro():
  """Función que actualiza datos de un libro del inventario"""
  mostrar_inventario()
  conexion = conectar()
  cursor = conexion.cursor()
  print()
  id_libro = int(input("Ingrese el ID del libro que desea actualizar: "))
  if libro_existe(conexion,'id',id_libro):
      cursor.execute("SELECT * FROM libros WHERE id = ?", (id_libro,))
      libro = cursor.fetchone()
      libro_sin_id = libro[1:] # Elimino el campo ID del libro para que no sea modificado
      libro_sin_id = modificar_datos(libro_sin_id)
      while True:
        mostrar_libro(libro_sin_id)
        accion = menu_confirmacion("actualizacion")
        if(accion=="confirmar"):
          break
        elif(accion=="modificar"):
          libro_sin_id = modificar_datos(libro_sin_id)
        else:
          print("\nActualizacion de libro cancelada.")
          input("\nPresione ENTER ⤵️   para continuar... ")
          conexion.close()
          return
      campos_sql = 'titulo = ?, autor = ?, categoria = ?, precio = ?, stock = ?'
      cursor.execute(f"UPDATE libros SET {campos_sql} WHERE id = ?", (*libro_sin_id, id_libro))
      conexion.commit()
      print()
      barra_progreso("ACTUALIZANDO")
      print("\nLibro actualizado exitosamente.")
      input("\nPresione ENTER ⤵️   para continuar... ")
  else:
      print(f"\nEl libro de ID {id_libro} no existe.")
      input("\nPresione ENTER ⤵️   para continuar... ")
  conexion.close() 

def remover_libro():
    """Función que remueve un libro del inventario"""
    mostrar_inventario()
    conexion = conectar()
    cursor = conexion.cursor()
    print()
    id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    # Verificar si el producto existe utilizando la función producto_existe
    if libro_existe(conexion,'id',id_libro):
        cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
        conexion.commit()
        print()
        barra_progreso("ELIMINANDO")
        print("\nLibro eliminado exitosamente.")
        input("\nPresione ENTER ⤵️   para continuar... ")
    else:
        print(f"\nEl libro de ID {id_libro} no existe.")
        input("\nPresione ENTER ⤵️   para continuar... ")
    conexion.close() 

def buscar_libro():
  pass

def bajo_stock():
  pass




def modificar_datos(libro):
  """Función que modifica los datos de un libro"""
  libro = list(libro)
  limpiar_consola()
  mostrar_libro(libro)
  campo = menu_edicion()
  limpiar_consola()
  if campo == 1:
    print(f"\nTITULO ACTUAL: {Fore.LIGHTGREEN_EX}{libro[0]}\n")
    libro[0] = input("🔤 Ingrese el nuevo titulo: ")
  elif campo == 2:
    print(f"\nAUTOR ACTUAL: {Fore.LIGHTGREEN_EX}{libro[1]}\n")
    libro[1] = input("🔤 Ingrese el nuevo autor: ") 
  elif campo == 3:
    print(f"\nCATEGORIA ACTUAL: {Fore.LIGHTGREEN_EX}{libro[2]}\n")
    libro[2] = menu_categorias()
  elif campo == 4:
    print(f"\nPRECIO ACTUAL: {Fore.LIGHTGREEN_EX}{'$'+str(libro[3])}\n")
    libro[3] = establecer_precio()
  elif campo == 5:
    print(f"\nSTOCK ACTUAL: {Fore.LIGHTGREEN_EX}{libro[4]}\n")
    libro[4] = establecer_stock()
  limpiar_consola()
  return tuple(libro)


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
  input("\nPresione ENTER ⤵️   para continuar... ")



#::::::::::::::: utilidades ::::::::::::::::

def nivel_stock(stock):
  """Función que define el color del valor del stock en el inventario"""
  if stock < 6: 
    return Fore.RED #si hay pocos libros se lo representa de color rojo
  elif stock < 15:
    return Fore.YELLOW
  else:
    return Fore.GREEN

def libro_existe(conexion,campo,valor):
  """Función que verifica si el libro existe en la base de datos"""
  cursor = conexion.cursor()
  cursor.execute(f"SELECT * FROM libros WHERE {campo} = ?", (valor,))
  libro = cursor.fetchall()
  return libro if libro else False

def es_decimal(cadena):
  """Función que verifica si el valor del precio ingresado es un número decimal"""
  if not cadena or cadena.count(".") > 1 or cadena[0] == ".":  # Verifica si la cadena está vacía
      return False
  partes = cadena.split(".")
  if not all(parte.isdigit() for parte in partes if parte) or len(partes) > 2:
      return False
  return True

def barra_progreso(mensaje):
  """Función que simula una barra de progreso visual"""
  tiempo_total = 2
  cantidad_puntos = 20
  intervalo = tiempo_total / cantidad_puntos
  print("\n")
  print(f"{mensaje +'⌛':^{cantidad_puntos}}")
  print('\u2500' * cantidad_puntos)
  print("\033[1B", end='')
  print('\u2500' * cantidad_puntos)
  print("\033[2A", end='')
  if(mensaje=="GUARDANDO"):
    color = Fore.GREEN
  elif(mensaje=="ELIMINANDO"):
    color = Fore.RED
  else:
    color = Fore.BLUE
  for _ in range(cantidad_puntos):
      print(color+'\u2588',end='', flush=True)
      time.sleep(intervalo)
  print("\n")


#::::::::::::::: programa principal ::::::::::::::::

while opcion != salir:
  limpiar_consola()
  opcion = menu_principal()

  if(opcion==1):
    ingresar_libro()
  elif(opcion==2): 
    mostrar_inventario()
    input("\nPresione ENTER ⤵️   para continuar... ")
  elif(opcion==3):
    actualizar_libro()
  elif(opcion==4):
    remover_libro()
  elif(opcion==5):
    buscar_libro()
  elif(opcion==6):
    bajo_stock()
  