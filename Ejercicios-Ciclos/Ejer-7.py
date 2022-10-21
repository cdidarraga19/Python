# Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:
'''
1
12
123
1234
12345
'''

numero = int(input("Digite un numero: "))
num = 5
for x in range(num):
    sum_1 = numero
    sum_2 = numero + numero
    sum_3 = numero + numero + numero
    sum_4 = numero + numero + numero + numero
    sum_5 = numero + numero + numero + numero + numero
else:
    print(f"\n {sum_1} \n {sum_1}{sum_2} \n {sum_1}{sum_2}{sum_3} \n {sum_1}{sum_2}{sum_3}{sum_4}  \n {sum_1}{sum_2}{sum_3}{sum_4}{sum_5}")
