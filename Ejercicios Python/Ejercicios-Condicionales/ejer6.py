# Solicitar tres números al usuario e imprimirlos en orden descendente (de mayor a menor).

num1 = float(input("Ingrese el numero uno: "))
num2 = float(input("Ingrese el numero dos: "))
num3 = float(input("Ingrese el numero tres: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"El numero mayor es: {num1}, el segundo es: {num2} y el menor de todos es: {num3}")

elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"El numero mayor es: {num2}, el segundo es: {num1} y el menor de todos es: {num3}")

elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f"El numero mayor es: {num3}, el segundo es: {num1} y el menor de todos es: {num2}")

elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f"El numero mayor es: {num3}, el segundo es: {num2} y el menor de todos es: {num1}")