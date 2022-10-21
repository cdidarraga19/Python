# Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.
lis = []
num = 10
for x in range(num):
    numero = int(input("Digite un numero: "))
    lis.append(numero)
else:
    suma = sum(lis)
    print(f"La suma de los numeros es {suma}")

    promedio = suma / 10
    print(f"El promedio de la suma es: {promedio}")