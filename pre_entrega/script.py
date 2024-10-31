
#Inventario de libros

import os

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

while opcion!=3:
  limpiar_consola()
  while True:
    print("")
    print("-"*30)
    print("INVENTARIO DE LIBROS")
    print("-"*30)
    print("[1] Ingresar un nuevo libro")
    print("[2] Mostrar inventario")
    print("[3] Salir")
    print("")
    opcion = input("Seleccione una opcion: ")
    if opcion.isdigit() or (opcion.startswith('-') and opcion[1:].isdigit()):
      opcion = int(opcion)
      if(opcion < 1 or opcion > 3):
        print(f"\n\"{opcion}\" no es una opcion valida, intente nuevamente")
        input("\nPresione ENTER para continuar... ")
        limpiar_consola()
      else:
        break
    else:
      print(f"\n\"{opcion}\" no es una opcion valida, intente nuevamente")
      input("\nPresione ENTER para continuar... ")
      limpiar_consola()

  if(opcion==1): #Ingreso de nuevo libro
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

  elif(opcion==2): #Visualizacion de inventario
    limpiar_consola()
    print("-"*30)
    print("INVENTARIO DE LIBROS")
    print("-"*30)
    print("x","-"*50,"x","-"*30,"x","-"*15,"x","-"*6,"x")
    print("| {:<50} | {:<30} | {:<15} | {:<6} |".format("Titulo", "Autor", "Categoria", "Stock"))
    print("x","-"*50,"x","-"*30,"x","-"*15,"x","-"*6,"x")
    num_libro=0
    while num_libro<len(inventario):
      print("| {:<50} | {:<30} | {:<15} | {:<6} |".format(inventario[num_libro][0], inventario[num_libro][1], inventario[num_libro][2], inventario[num_libro][3]))
      num_libro+=1
    print("x","-"*50,"x","-"*30,"x","-"*15,"x","-"*6,"x")
    input("\nPresione ENTER para continuar... ")
    limpiar_consola()

