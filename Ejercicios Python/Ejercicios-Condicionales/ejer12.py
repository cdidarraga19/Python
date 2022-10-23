# El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio 
# aeróbico se calcula con la fórmula: Género femenino (1): número de pulsaciones = (220 -edad en años)/10
# Género masculino (2): número de pulsaciones = (210 -edad en años)/10 Lea la edad y el género y 
# muestre el número de pulsaciones.

print(" Digite F si es genero femenino, digite M si es genero Masculino --")

edad = int(input("Digite su edad: "))
genero = int(input("Digite su genero: "))

if genero == 1:
    pulsaciones =(220 - edad) / 10
    print(f"Su genero es femenino y su edad es de: {edad}, sus pulsaciones cada 10 segundos en base a su edad son de: {pulsaciones}")
elif genero == 2:
    pulsaciones = (210 - edad) / 10 
    print(f"Su genero es masculino y su edad es de: {edad}, sus pulsaciones cada 10 segundos en base a su edad son de:{pulsaciones}")