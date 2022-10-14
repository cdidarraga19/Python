# Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC 
# de una persona que se calcula con la fórmula IMC=P/T2en donde P es el peso en Kg. 
# y T esla talla en metros. 
# Lea un valor de P y de T, calcule el IMC y muestre su estado según la siguiente tabla:

from cgi import print_environ


talla = float(input("Ingrese su talla: "))
peso = float(input("Ingrese su peso: "))

formula = peso / (talla**2)

if formula < 20:
    print("Usted esta desnutrido")
elif formula >= 20 and formula < 25:
    print("Usted tiene un peso normal")
elif formula >= 25 and formula < 30:
    print("Usted tiene sobrepeso")
elif formula >= 30 and formula < 35:
    print("Usted se encuentra en el grado 1 de obesidad")
elif formula >= 35 and formula < 40:
    print("Usted se encuentra en el grado 2 de obesidad")
else:
    print("Usted se encuentra en el grado 3 de obesidad")