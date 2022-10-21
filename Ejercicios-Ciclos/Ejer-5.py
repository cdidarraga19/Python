# Escriba un programa para mostrar la tabla de multiplicar de un entero dado.

num = 10
cont = 0
nume = int(input("Ingrese un numero entero: "))

while cont < 10:
    cont += 1
    print (f"{nume} * {cont} = {nume * cont}")