# Aplicación para realizar calculos simples, suma, resta, multiplicación y división. 
# La app puede realizar calculos de a dos numero por vez.
# Es decir podria operar a + b, pero no a + b + c

# Defino el primer numero con el cual voy a operar
import math

n1 = 2
n2 = 3

def verifico_n1():
    while True:
        try:
            n1 = int(input("Seleccione numero 1 : "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        else:
            print(n1)
            break
        continue

def verifico_n2():
    while True:
        try:
            n2 = int(input("Seleccione numero 2 : "))
        except ValueError:
            print("Debes escribir un numero")
            continue
        else:
            print(n2)
            break
        continue


def resultado(): 
    if operacion == "+" :
        print(suma)
    elif operacion == "-":
        print(resta)
    elif operacion == "*":
        print(multiplicacion)
    elif operacion == "/":
        print(division)

print("Esta es una calculadora para relizar operaciones simples")
print("Escriba el primer numero, luego selecione la operación, y luego el siguiente numero")

verifico_n1()
operacion = (input("Seleccione una operación: "))
verifico_n2()


suma = n1+n2
resta = n1-n2
division = n1/n2
multiplicacion = n1*n2

resultado()





