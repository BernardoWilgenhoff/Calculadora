# Aplicación para realizar calculos simples, suma, resta, multiplicación y división. 
# La app puede realizar calculos de a dos numero por vez.
# Es decir podria operar a + b, pero no a + b + c

# Defino el primer numero con el cual voy a operar
import math

n1 = ""
n2 = ""

def verifico_n1():
    global n1
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
    global n2
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
        print("La suma de ", n1, "+", n2, "=", suma)
    elif operacion == "-":
        print("La resta de ", n1, "-", n2, "=", resta)
    elif operacion == "*":
        print("La multiplicación de ", n1, "*", n2, "=", multiplicacion)
    elif operacion == "/":
        print("La división de ", n1, "/", n2, "=", division)

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






