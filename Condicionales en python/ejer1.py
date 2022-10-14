# Par o impar. Solicitar número al usuario y determinar si es par, impar o es cero.
 
def check(num): 
    if num & 1 == 0:
        print("Par")
    else:
        print("Impar")
check(0)