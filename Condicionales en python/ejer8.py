# Leer el número de llantas de una compra y mostrar el valor que debe pagarse. 
# El almacén las vende con  la  siguiente  política:  Si  se  compran  menos  de  5  llantas,
# el  precio  unitario  es $240000. Si  se compran 6 o 7, el precio unitario es $221000,
# y si se compran más de 7 llantas, elprecio unitario es $180000.

llant = int(input("Bienvenido, cuantas llantas desea llevar? "))

if llant <= 5 :
    print(f"Señor cliente, usted solicitó {llant} llantas, el precio unitario de estas es de '$240000', su precio total sería de: {240000 * llant}")
elif llant == 6 or llant == 7:
    print(f"Señor cliente, usted solicitó {llant} llantas, el precio unitario de estas es de $221000, su precio total sería de: {221000 * llant}")
else:
    print(f"Señor cliente, usted solicitó {llant} llantas, el precio unitario de estas es de $180000, su precio total sería de: {180000 * llant}")