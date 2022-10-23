print("Ingrese el primer producto")
prod1 = input()
print(f"Cantidad comprada de {prod1}")
prod1_cant = int(input())
print(f"Valor de la unidad de {prod1_cant}")
prod1_vu

print("Ingrese el primer producto")
prod2 = input()
print(f"Cantidad comprada de {prod2}")
prod2_cant = int(input())
print(f"Valor de la unidad de {prod2_cant}")
prod2_vu

print("Ingrese el primer producto")
prod3 = input()
print(f"Cantidad comprada de {prod3}")
prod3_cant = int(input())
print(f"Valor de la unidad de {prod3_cant}")
prod3_vu

prod1_st = prod1_st * prod1_vu
prod2_st = prod2_st * prod2_vu
prod3_st = prod3_st * prod3_vu

subT = prod1_st + prod2_st + prod3_st
iva = subT * 16
tot = subT + iva

print("El total a pagar por ",prod1,"es de: ",prod1_st)
print("El total a pagar por ",prod2,"es de: ",prod2_st)
print("El total a pagar por ",prod3,"es de: ",prod3_st)
print("El subtotal de la factura es",subT)
print("El iva fue de",iva)
print("El total a pagar con el iva includo es: ",tot)