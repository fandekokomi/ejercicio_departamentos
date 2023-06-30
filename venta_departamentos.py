from funciones import *
precio1 = 150000000
precio2 = 200000000
total = 0
total_ganancias = 0
while True:
    os.system("cls")
    opcion = menu()
    if opcion ==1:
        os.system("cls")
        ver_edificio(edificio)
    elif opcion ==2:
        total_ganancias += compraredificio(precio1,precio2,total)
    elif opcion ==3:
        verdatos(lruts,lnombres,lpisos,ldepartamentos)
    elif opcion ==4:
        print(f"Total de ganancias obtenidas: ${total_ganancias}")
        print("\n Presione una tecla para continuar....")
        tecla.getch()
    else:
        break