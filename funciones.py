import os
import time
import msvcrt as tecla
from numpy import *
import random
import re
import os
import msvcrt as tecla
edificio = zeros((10,4), int)
lruts = []
lnombres = []
lpisos = []
ldepartamentos = []
def compraredificio(precio1,precio2,total):
    os.system("cls")
    if 0 not in edificio:
        return
    rut = validar_rut()
    if rut in lruts:
        for x in range(len(lruts)):
            if rut == lruts[x]:
                posicion = x
        print("Hola Denuevo!", lnombres[posicion])
        time.sleep(5)
        while True:
            ver_edificio(edificio)
            piso = validar_piso(1,10)
            departamento = validar_departamento("A","B","C","D")
            if departamento.upper() == "A":
                if edificio[piso-1][0] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][0] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
            elif departamento.upper() == "B":
                if edificio[piso-1][1] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][1] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
            elif departamento.upper() == "C":
                if edificio[piso-1][2] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][2] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
            else:
                if edificio[piso-1][3] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][3] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
        lpisos[posicion] = lpisos[posicion] + "," + str(piso)
        ldepartamentos[posicion] = ldepartamentos[posicion] + "," + departamento.upper()
        return total
    else:
        nombre = validar_nombre()
        while True:
            ver_edificio(edificio)
            piso = validar_piso(1,10)
            departamento = validar_departamento("A","B","C","D")
            if departamento.upper() == "A":
                if edificio[piso-1][0] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][0] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
            elif departamento.upper() == "B":
                if edificio[piso-1][1] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][1] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
            elif departamento.upper() == "C":
                if edificio[piso-1][2] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][2] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
            else:
                if edificio[piso-1][3] == 0:
                    total = validar_compra(piso,precio1,precio2,total)
                    edificio[piso-1][3] = 1
                    break
                else:
                    print("Departamento ocupado! por favor elija otro departamento o piso!")
        lruts.append(rut)
        lnombres.append(nombre)
        lpisos.append(str(piso))
        ldepartamentos.append(departamento.upper())
        return total
def verdatos(lruts,lnombres,lpisos,ldepartamentos):
    os.system("cls")
    rut = validar_rut()
    if rut in lruts:
        for x in range(len(lruts)):
            if rut == lruts[x]:
                posicion = x
    print("Nombre:",lnombres[posicion])
    print("DEPARTAMENTOS ASOCIADOS AL RUT:",rut)
    print("PISOS:",lpisos[posicion])
    print("DEPARTAMENTOS:",ldepartamentos[posicion])
    print("\n Presione una tecla para continuar")
    tecla.getch()
    os.system("cls")
def validar_compra(piso,precio1,precio2,total):
    if piso in(8,9,10):
        efectivo = validar_efectivo(precio2)
        total += precio2
        if efectivo > precio2:
            vuelto = efectivo - precio2
            print(f"Su vuelto es de ${vuelto}")
        print("\n Ingrese cualquier tecla para continuar...")
        tecla.getch()
        return total
    else:
        efectivo = validar_efectivo(precio1)
        total += precio1
        if efectivo > precio1:
            vuelto = efectivo - precio1
            print(f"Su vuelto es de ${vuelto}")
        print("\n Ingrese cualquier tecla para continuar...")
        tecla.getch()
        return total
def validar_efectivo(total:int):
    while True:
        try:
            efectivo = int(input(f"El total es: ${total} \nIngrese efectivo para pagar: "))
            if efectivo < total:
                print("El dinero ingresado es insuficiente, intente nuevamente!")
            else:
                print("Gracias por pagar!")
                return efectivo
        except:
            print("Ingrese un monto valido!")
def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def ver_edificio(edificio):
    os.system("cls")
    print("        Edificio: ")
    print("       DEPARTAMENTOS ")
    print("           A B C D")
    for x in reversed(range(10)):
        print("  PISO", str(x+1).ljust(2), end=": ")
        for y in range(4):
            print(edificio[x][y], end=" ")
        print()
    print("\nPresione una tecla para continuar...")
    tecla.getch()
def validar_departamento(letra1:str,letra2:str,letra3:str,letra4:str):
    while True:
        departamento = input(f"Ingrese letra de departamento ({letra1},{letra2},{letra3},{letra4}): ")
        if departamento.isalpha() and departamento.upper() in (letra1, letra2, letra3, letra4):
            return departamento
        else:
            print("ERROR! DEPARTAMENTO INCORRECTO!")
def validar_piso(min:int,max:int):
    while True:
        try:
            piso = int(input(f"Ingrese número de piso ({min},{max}):"))
            if piso >= min and piso <= max:
                return piso
            else:
                print("ERROR! PISO INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def menu():
    print("""MENÚ:
    1. Ver edificio
    2. Comprar Edificio
    3. Buscar dueño
    4. Total de ganancias
    5. Salir""")
    opcion = validar_opcion(1,5)
    return opcion
def validar_opcion(min:int,max:int):
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= min and opcion <= max:
                    return opcion
                else:
                    print("¡ERROR! ¡OPCIÓN INCORRECTA!")
            except:
                print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")