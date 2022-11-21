# Aplicación para realizar calculos simples, suma, resta, multiplicación y división. 
# La app puede realizar calculos de a dos numero por vez.
# Es decir podria operar a + b, pero no a + b + c

# Defino el primer numero con el cual voy a operar
import math
from tkinter import N, Y
from unittest import result

n1 = ""
n2 = ""
numero_1 = ""
operacion = ""

def verifico_n1():
    global n1
    while True:
        try:
            n1 = float(input("Seleccione numero 1 : "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        else:
            print(n1)
            break
        continue

def verifico_n2():
    global n2
    while True:
        try:
            n2 = float(input("Seleccione numero 2 : "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        else:
            print(n2)
            break
        continue

def verifico_operacion():
    global operacion
    while True:
        operacion = (input("Seleccione una operación: "))
        if operacion != "+" "-" "*" "/":
            print("Debe seleccionar una operación válida + - * /")
        else:
            break
        continue


def resultado(): 
    global numero_1
    if operacion == "+":
        suma = n1+n2
        print("La suma de ", n1, "+", n2, "=", suma)
        numero_1 = suma
    elif operacion == "-":
        resta = n1-n2
        print("La resta de ", n1, "-", n2, "=", resta)
        numero_1 = resta
    elif operacion == "*":
        multiplicacion = n1*n2
        print("La multiplicación de ", n1, "*", n2, "=", multiplicacion)
        numero_1 = multiplicacion
    elif operacion == "/":
        division = n1/n2
        print("La división de ", n1, "/", n2, "=", division)
        numero_1 = division


#Comienza la APP con un msj de bienvenida, ,luego ejecuta

print("Esta es una calculadora para relizar operaciones simples")
print("Escriba el primer numero, luego selecione la operación, y luego el siguiente numero")

while True: 
    verifico_n1()
    verifico_operacion()
    verifico_n2()
    resultado()
    resetear = input("Si desea resetar oprima Y, si quiere seguir ejecutando N")
    
    while resetear == N:
        n1 = numero_1
        print(n1)
        verifico_operacion()
        verifico_n2()
        resultado()
        resetear = input("Si desea resetar oprima Y, si quiere seguir ejecutando N")
    else:
        continue
