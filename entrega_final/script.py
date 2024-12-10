#Inventario de libros

import os
import sqlite3 # importamos modulo

print('SQLite version:',sqlite3.sqlite_version) # vemos version
conn = sqlite3.connect('inventario.db')

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

inventario = [ #Contiene: Titulo - Autor - Categoria - Stock
  ["Fuego y Sangre","George R.R. Martin","Fantasia",30],
  ["El Hobbit","J.R.R. Tolkien","Fantasia",25],
  ["Orgulo y Prejuicio","Jane Austen","Romance",10],
  ["Harry Potter y la Piedra Filosofal","J.K. Rowling","Fantasia",15],
  ["Misery","Stephen King","Terror",10],
  ["Los Crimenes de la Calle Morgue","Edgar Allan Poe","Policial",13],
  ["La Guerra de los Mundos","H.G. Wells","Ciencia Ficcion",24]
]

opcion = None
opcion_min = 1
opcion_max = 7
salir = 7

def imprimir_menu():
  print("")
  print("-"*30)
  print("INVENTARIO DE LIBROS")
  print("-"*30)
  print("[1] Ingresar un nuevo libro")
  print("[2] Mostrar inventario")
  print("[3] Actualizar libro")
  print("[4] Remover libro")
  print("[5] Buscar libro")
  print("[6] Reporte bajo stock")
  print("[7] Salir")
  print("")


def menu():
  while True:
    imprimir_menu()
    opc = input("Seleccione una opcion: ")
    if opc.isdigit() or (opc.startswith('-') and opc[1:].isdigit()):
      opc = int(opc)
      if(opc >= opcion_min and opc <= opcion_max):
        break
    print(f"\n\"{opc}\" no es una opcion valida, intente nuevamente")
    input("\nPresione ENTER para continuar... ")
    limpiar_consola()
  return opc

def ingresar_libro():
  limpiar_consola()
  titulo = input("\nIngrese el titulo: ")
  autor = input("\nIngrese el autor: ").title()
  while True:
    limpiar_consola()
    print("\nCategorias: [Terror - Ciencia Ficcion - Romance - Fantasia - Policial]\n")
    categoria = input("Ingrese la categoria: ").title()
    if(categoria=="Terror" or categoria=="Ciencia Ficcion" or categoria=="Romance" or categoria=="Fantasia" or categoria=="Policial"):
      break
    print(f"\n\"{categoria}\" no es una categoria valida, intente nuevamente")
    input("\nPresione ENTER para continuar... ")
  while True:
    limpiar_consola()
    stock = input("\nIngrese la cantidad: ")
    if stock.isdigit() or (stock.startswith('-') and stock[1:].isdigit()):
      num = int(stock)
      if(num > 0):
        break
    else:
      print("\nError: La cantidad debe ser un numero entero mayor a cero.")
      input("\nPresione ENTER para continuar... ")
  
  libro = [titulo,autor,categoria,stock]
  inventario.append(libro)

def mostrar_inventario():
  limpiar_consola()
  print(f"\n{'INVENTARIO DE LIBROS':^95}\n")
  print("+","-"*45,"+","-"*25,"+","-"*15,"+","-"*6,"+")
  print(f"| {'Titulo':<45} | {'Autor':<25} | {'Categoria':<15} | {'Stock':<6} |")
  print("+","-"*45,"+","-"*25,"+","-"*15,"+","-"*6,"+")
  num_libro=0
  while num_libro<len(inventario):
    print(f"| {inventario[num_libro][0]:<45} | {inventario[num_libro][1]:<25} | {inventario[num_libro][2]:<15} | {inventario[num_libro][3]:<6} |")
    num_libro+=1
  print("+","-"*45,"+","-"*25,"+","-"*15,"+","-"*6,"+")
  input("\nPresione ENTER para continuar... ")
  limpiar_consola()

def actualizar_libro():
  pass

def remover_libro():
  pass

def buscar_libro():
  pass

def bajo_stock():
  pass


while opcion != salir:
  limpiar_consola()
  opcion = menu()

  if(opcion==1):
    ingresar_libro()
  elif(opcion==2): 
    mostrar_inventario()
  elif(opcion==3):
    actualizar_libro()
  elif(opcion==4):
    remover_libro()
  elif(opcion==5):
    buscar_libro()
  elif(opcion==6):
    bajo_stock()