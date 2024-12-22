
import os
import time
from colorama import Fore, Style, Back, init
init(autoreset=True)


#::::::::::::::: utilidades ::::::::::::::::

def limpiar_consola():
    """Función que limpia la consola"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def nivel_stock(stock):
    """Función que define el color del valor del stock en el inventario"""
    if stock < 10: 
        return Fore.RED #si hay pocos libros se lo representa de color rojo
    elif stock < 20:
        return Fore.YELLOW 
    else:
        return Fore.GREEN #si hay suficientes libros se lo representa de color verde

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
        color = Fore.GREEN #si la barra es de guardado, se lo representa de color verde
    elif(mensaje=="ELIMINANDO"):
        color = Fore.RED #si la barra es de eliminacion, se lo representa de color rojo
    else:
        color = Fore.BLUE #si la barra es de busqueda, se lo representa de color azul
    for _ in range(cantidad_puntos):
        print(color+'\u2588',end='', flush=True)
        time.sleep(intervalo)
    print("\n")


#::::::::::::::: visualizacion de datos ::::::::::::::::

def imprimir_marco_inventario(filas):
    """Imprime un marco visual para el inventario de libros."""
    print("\u2554" + "\u2550"*5 + "\u2566" + "\u2550"*47 + "\u2566" + "\u2550"*27 + "\u2566" + "\u2550"*17 + "\u2566" + "\u2550"*12 + "\u2566" + "\u2550"*7 + "\u2557")
    print(f"\u2551 {'ID':<3} \u2551 {'Titulo':<45} \u2551 {'Autor':<25} \u2551 {'Categoria':<15} \u2551 {'Precio':<10} \u2551 {'Stock':<5} \u2551")
    print("\u2560" + "\u2550"*5 + "\u256C" + "\u2550"*47 + "\u256C" + "\u2550"*27 + "\u256C" + "\u2550"*17 + "\u256C" + "\u2550"*12 + "\u256C" + "\u2550"*7 + "\u2563")
    for _ in range(filas):
        print(f"\u2551 {' ':<3} \u2551 {' ':<45} \u2551 {' ':<25} \u2551 {' ':<15} \u2551 {' ':<10} \u2551 {' ':<5} \u2551")
    print("\u255A" + "\u2550"*5 + "\u2569" + "\u2550"*47 + "\u2569" + "\u2550"*27 + "\u2569" + "\u2550"*17 + "\u2569" + "\u2550"*12 + "\u2569" + "\u2550"*7 + "\u255D")
    print(f"\033[{filas+1}A", end='') #mueve el cursor hacia arriba usando secucnias ANSI

def mostrar_libro(libro):
    """Muestra los datos de un libro en particular."""
    print(f"\n{'DATOS DEL LIBRO 📖':^117}\n")
    print("\u2554" + "\u2550"*47 + "\u2566" + "\u2550"*27 + "\u2566" + "\u2550"*17 + "\u2566" + "\u2550"*12 + "\u2566" + "\u2550"*7 + "\u2557")
    print(f"\u2551 {Back.WHITE+Fore.BLACK}{'Titulo':^45}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Autor':^25}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Categoria':^15}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Precio':^10}{Style.RESET_ALL} \u2551 {Back.WHITE+Fore.BLACK}{'Stock':^5}{Style.RESET_ALL} \u2551")
    print("\u2560" + "\u2550"*47 + "\u256C" + "\u2550"*27 + "\u256C" + "\u2550"*17 + "\u256C" + "\u2550"*12 + "\u256C" + "\u2550"*7 + "\u2563")
    print(f"\u2551 {libro[0]:^45} \u2551 {libro[1]:^25} \u2551 {libro[2]:^15} \u2551 {'$'+str(libro[3]):^10} \u2551 {libro[4]:^5} \u2551")
    print("\u255A" + "\u2550"*47 + "\u2569" + "\u2550"*27 + "\u2569" + "\u2550"*17 + "\u2569" + "\u2550"*12 + "\u2569" + "\u2550"*7 + "\u255D")

def mostrar_libros_bajo_stock(libros):
    # Muestra los libros con bajo stock
    print(f"\n{'LIBROS CON BAJO STOCK 📖':^117}\n")
    imprimir_marco_inventario(len(libros))
    num_libro=0
    color = Fore.RED
    while num_libro<len(libros):
        print(f"\033[2C{libros[num_libro][0]:<3} \033[1C {libros[num_libro][1]:<45} \033[1C {libros[num_libro][2]:<25} \033[1C {libros[num_libro][3]:<15} \033[1C ${libros[num_libro][4]:<9} \033[1C {color}{libros[num_libro][5]:<5}{Style.RESET_ALL}")
        num_libro+=1

def mostrar_resultados_busqueda(libros):
    # Muestra los libros enconrtados mediante una busqueda realizada por el usuario
    print(f"\n{'RESULTADOS 🔍':^117}\n")
    imprimir_marco_inventario(len(libros))
    num_libro=0
    color = nivel_stock(libros[num_libro][5])
    while num_libro<len(libros):
        print(f"\033[2C{libros[num_libro][0]:<3} \033[1C {libros[num_libro][1]:<45} \033[1C {libros[num_libro][2]:<25} \033[1C {libros[num_libro][3]:<15} \033[1C ${libros[num_libro][4]:<9} \033[1C {color}{libros[num_libro][5]:<5}{Style.RESET_ALL}")
        num_libro+=1