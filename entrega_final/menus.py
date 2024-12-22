
from colorama import Fore, Style, Back, init
init(autoreset=True)

from utilidades import limpiar_consola


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
    #imprimo el marco y me posiciono en la fila 3 para posteriorente escribir el contenido

def imprimir_menu_principal():
    """Muestra las opciones del menu principal"""
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
    print(f"\033[1C{Style.BRIGHT}{'CAMPOS EDITABLES  ✏️':^47}\n\n")
    print(f"\033[2C [{Fore.YELLOW}{'1'}{Style.RESET_ALL}] {'Titulo'}")
    print(f"\033[2C [{Fore.YELLOW}{'2'}{Style.RESET_ALL}] {'Autor'}")
    print(f"\033[2C [{Fore.YELLOW}{'3'}{Style.RESET_ALL}] {'Categoria'}")
    print(f"\033[2C [{Fore.YELLOW}{'4'}{Style.RESET_ALL}] {'Precio'}")
    print(f"\033[2C [{Fore.YELLOW}{'5'}{Style.RESET_ALL}] {'Stock'}\n")
    print("\033[3C", end='')

def imprimir_menu_busqueda():
    """Muestra el menú de seleccion de criterio de busqueda."""
    imprimir_marco(8)
    print(f"\033[1C{Style.BRIGHT}{'CRITERIO DE BUSQUEDA 🔍':^46}\n\n")
    print(f"\033[2C [{Fore.YELLOW}{'1'}{Style.RESET_ALL}] {'ID'}")
    print(f"\033[2C [{Fore.YELLOW}{'2'}{Style.RESET_ALL}] {'Titulo'}")
    print(f"\033[2C [{Fore.YELLOW}{'3'}{Style.RESET_ALL}] {'Autor'}")
    print(f"\033[2C [{Fore.YELLOW}{'4'}{Style.RESET_ALL}] {'Categoria'}\n")
    print("\033[3C", end='')


#::::::::::::::: logica de menus ::::::::::::::::

def menu_principal():
    """Muestra el menu principal y retorna la opcion seleccionada."""
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
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
    return opc

def menu_categorias():
    """Muestra el menú de seleccion de categoria."""
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
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
    limpiar_consola()
    return categorias_validas[opc-1] #retorna la categoria seleccionada, valida la entrada del usuario

def menu_confirmacion(menu_tipo):
    """ Muestra el menu de confirmacion de ingreso al inventario"""
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
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
    return acciones[opc-1] #retorna la accion seleccionada, valida la entrada del usuario

def menu_edicion():
    """Muestra el menu de seleccion de campo a editar."""
    campos = ("titulo","autor","categoria","precio","stock")
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
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
    return campos[opc-1] #retorna el campo seleccionado, valida la entrada del usuario

def menu_busqueda():
    """Muestra el menu de seleccion de criterio de busqueda."""
    criterios = ("id","titulo","autor","categoria")
    opcion_min = 1
    opcion_max = 4
    while True:
        imprimir_menu_busqueda()
        opc = input("Seleccione el criterio de busqueda: ")
        if opc.isdigit() or (opc.startswith('-') and opc[1:].isdigit()):
            opc = int(opc)
            if(opc >= opcion_min and opc <= opcion_max):
                break
        print(f"\n\"{opc}\" no es una opcion valida 🚫, intente nuevamente")
        input("\nPresione ENTER ⤵️  para continuar... ")
        limpiar_consola()
    limpiar_consola()
    return criterios[opc-1] #retorna el criterio seleccionado, valida la entrada del usuario