n = int(input("¿Cuantos valores desea ingresar? "))
suma = 0
i=1
while(i <= n):
    print("ingrese el valor del numero: ",i)
    num = float(input())
    suma = suma+num
    i+=1
prom = suma / n
print(f"El promedio de los numeros es {prom}")