# Un  local  vende  sus  productos  con  la siguiente  promoción.
# Si  compra  hasta  5  artículos,  no  hay descuento. Si compra más de 5 artículos, 
# pero menos de 10, el precio unitario se reduce en 5%. Si compra 10 o más artículos, 
# el precio unitario se reduce en 8%. Ingrese un dato de cantidad 
# y el valor del precio unitario original. Calcule y muestre el valor total apagar.

cant = int(input("Ingrese la cantidad de los productos: "))
val_uni = int(input("Ingrese el precio unitario de los producto: "))
prec_tot = val_uni * cant

if cant <= 5:
    print(f"Sus articulos a llevar son: {cant}, el precio unitario es: {val_uni}, el monto total de la compra es: {prec_tot}")
if cant > 5 and cant <= 10:
    desc = 0.5
    prec_desc = int(prec_tot * desc)

    print(f"Sus articulos a llevar son: {cant}, el precio unitario es: {val_uni}, tiene un descuento del 5%, donde el monto total de la compra es: {prec_desc}")

elif cant > 10:
    desc = 0.8
    prec_desc = int(prec_tot * desc)
    print(f"Sus articulos a llevar son: {cant}, el precio unitario es: {val_uni}, el descuento es del 8%, el monto total de la compra es: {prec_desc}")