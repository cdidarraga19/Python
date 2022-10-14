# Solicitar número al usuario y determinar si es negativo, positivo o cero.
numero = int(input("Ingrese su numero: "))

if numero > 0:
    print("El número:", numero, "es positivo")
elif numero < 0:
    print("El número:", numero, "es negativo")
else:
    print("El número:", numero, "es neutro")