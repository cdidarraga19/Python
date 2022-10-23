# Programa que permita a un usuario tomar una decisión del tipo de pago a usar.
# Si la cuenta es menor a  $150000 pago  en  efectivo.  
# Sino,  si  es  de  $150000 hasta  $300000 pago con  el  celular (dinero electrónico). 
# Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Caso contrario, 
# pago con la tarjeta de crédito.

cuenta = int(input("Ingrese el valor de la cuenta: "))

if cuenta < 150000:
    print(f"¡Bienvenido! :), su cuenta es de: {cuenta}, puede generar el pago en efectivo")
elif cuenta >= 150000 and cuenta < 300000:
    print(f"¡Bienvenido! :), su cuenta es de: {cuenta}, puede generar el pago en efectivo o pago por celular")
elif cuenta >= 300000 and cuenta <= 600000:
    print(f"¡Bienvenido! :), su cuenta es de: {cuenta}, puede generar el pago en efectivo, pago por celular o tarjeta débito")
else:
    print(f"¡Bienvenido! :), su cuenta es de: {cuenta}, puede generar el pago en efectivo, pago por celular, tarjeta débito o crédito")