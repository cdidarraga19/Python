# El precio que debe pagar un cliente por una  pizza  depende  del tamaño seleccionado,  
# como  se muestra a continuación:
# Tamaño    Precio
#   1      $15.000
#   2      $24.000
#   3      $36.000

# Si  cada  ingrediente  adicional cuesta  $4.000. Escribir  un  programa  que solicite  al  empleado 
# encargado de registrarlas ventas, el tamaño de la pizza y el número de ingredientes adicionales y 
# muestre al cliente el precio que debe pagar.

pizza_t = int(input("Por favor, escriba el tamaño de la pizza, los rangos van de 1 a 3: "))
ingred = int(input("Por favor, digite el numero de ingredientes a adicionar: "))

multipli =  4000 * ingred

if pizza_t == 1:
    precio = 15000
    print(f"Su monto a pagar es de: {precio + multipli}")

elif pizza_t == 2:
    precio = 24000
    print(f"Su monto a pagar es de: {precio + multipli}")

elif pizza_t == 3:
    precio = 36000
    print(f"Su monto a pagar es de: {precio + multipli}")

else:
    print("Error, esta digitando un valor fuera de rango, se reiniciará el servicio.")
