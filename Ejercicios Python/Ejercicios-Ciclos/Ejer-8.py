# Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1.
'''
   1
  2 3
 4 5 6
7 8 9 10
'''

numPi = int(input("Digite un numero: "))

for x in range(1):
    print(f"   {numPi}")
    print(f"  {numPi + 1} {numPi + 2}")
    print(f" {numPi + 3} {numPi + 4} {numPi + 5}")
    print(f"{numPi + 6} {numPi + 7} {numPi + 8} {numPi + 9}")
