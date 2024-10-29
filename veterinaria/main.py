registros = []

cant_registros = 25
opcion = 0
num_registro = 0

while True:
    while True:
      print("\nMENU\n")
      print("[1] Ingresar datos")
      print("[2] Salir e imprimir resultados")
      opcion = int(input("\nElija una opcion: "))
      if(opcion!=1 and opcion!=2):
          print(f"{opcion} no es una opcion válida\n")
      else:
          break
    if(opcion==1):
        if(cant_registros!=0):
            while True:
              edad = int(input("\nIngrese la edad: "))
              if(edad >= 1 or edad<=25):
                  break
              else:
                  print("ERROR, edad no válida\n")
    
            while True:
                print("\nTipos: [perro - gato - loro]\n")
                tipo = input("Ingrese el tipo: ").lower()
                if(tipo=="gato" or tipo=="perro" or tipo=="loro"):
                    break
                else:
                    print(tipo)
                    print("ERROR, tipo no válido\n")
            
            while True:
                peso=float(input("Ingrese el peso: "))
                if(peso>0):
                    break
                else:
                    print("ERROR, el peso debe ser mayor a cero\n")
            
            while True:
                print("\nDiagnosticos: [problemas digestivos - parasitos - infeccion]\n")
                diagnostico=input("Ingrese el diagnostico: ").lower()
                if(diagnostico=="problemas digestivos" or diagnostico=="parasitos" or diagnostico=="infeccion"):
                    break
                else:
                    print(diagnostico)
                    print(f"ERROR, {diagnostico} no es un diagnostico válido\n")
            
            while True:
                vacuna = input("Está vacunado/a? [si-no]: ").lower()
                if(vacuna=="si" or vacuna=="no"):
                    break
                else:
                    print(f"ERROR, {vacuna} no es una respuesta válida\n")
            
            mascota = [edad, tipo, peso, vacuna, diagnostico]
            registros.append(mascota)
            
            cant_registros-=1
        else:
            print("\nLos 25 registros ya fueron ocupados\n")
    else:
        print("\nEdad\tTipo\tPeso\tVacuna\tDiagnostico\n")
        print("-"*45)
        while num_registro<len(registros):
            print(f"{registros[num_registro][0]}\t{registros[num_registro][1]}\t{registros[num_registro][2]}\t{registros[num_registro][3]}\t{registros[num_registro][4]}")
            num_registro+=1
        break
        