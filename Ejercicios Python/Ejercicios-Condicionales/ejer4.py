# Solicitar cinco (5) notas de 0.0 a 5.0 a un estudiante y calcular promedio.
# Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0.

print("Ingesar sus cinco notas desde 0.0 hasta 5.0 ")

num1 = float(input("Ingrese su primera nota: "))
num2 = float(input("Ingrese su segunda nota: "))
num3 = float(input("Ingrese su tecera nota: "))
num4 = float(input("Ingrese su cuarta nota: "))
num5 = float(input("Ingrese su quinta nota: "))

promedio = (num1 + num2 + num3 + num4 + num5) / 5

if promedio > 5.0:
    print("Ingrese las notas")
elif promedio >= 3.0 and promedio <= 5.0:
    print("Aprobó")
else:
    print("Reprobó")

    
