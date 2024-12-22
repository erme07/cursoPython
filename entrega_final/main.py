# Entrega final del curso de Python de Talento Tech
# Medina Erik

from funciones_principales import *

datos = [
    ("Fuego y Sangre","George R.R. Martin","Fantasia",25500,30),
    ("El Hobbit","J.R.R. Tolkien","Fantasia",36300,25),
    ("Orgullo y Prejuicio","Jane Austen","Romance",21100,6),
    ("Harry Potter y la Piedra Filosofal","J.K. Rowling","Fantasia",63700,15),
    ("Misery","Stephen King","Terror",27700,8),
    ("Los Crimenes de la Calle Morgue","Edgar Allan Poe","Policial",10450,10),
    ("La Guerra de los Mundos","H.G. Wells","Ciencia Ficcion",5400,24)
]#libros de relleno para la base de datos

opcion = None
salir = 7

crear_tabla()
cargar_datos_iniciales(datos) #carga los libros de relleno en la base de datos, solo si está vacia

while opcion != salir:
    limpiar_consola()
    opcion = menu_principal() #muestra el menu principal y retorna la opcion seleccionada
    if(opcion==1):
        ingresar_libro()
    elif(opcion==2): 
        mostrar_inventario()
        input("\nPresione ENTER ⤵️  para continuar... ")
    elif(opcion==3):
        actualizar_libro()
    elif(opcion==4):
        remover_libro()
    elif(opcion==5):
        buscar_libro()
    elif(opcion==6):
        bajo_stock()