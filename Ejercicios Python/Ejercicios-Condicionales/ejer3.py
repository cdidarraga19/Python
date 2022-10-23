# Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir los resultados.

numero1 = int(input("Ingrese su primer numero: "))
numero2 = int(input("Ingrese su segundo numero: "))

if numero1 > numero2:
    print (numero1,"es mayor que", numero2)
elif numero1 < numero2:
    print (numero1,"es menor que", numero2)
