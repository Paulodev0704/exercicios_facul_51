import os
cont = 0
maior_numero = 0
menor_numero = 10000000
for i in range(1,6): 
    num = int(input("Digite um numero: "))
    if num > maior_numero:
        maior_numero = num
    elif num < menor_numero:
        menor_numero = num
    else:
        print("Digite apenas numeros inteiros.")
    
    cont = cont + 1

os.system("cls")

print(f"Dentre os {cont} numeros, o maior foi: {maior_numero} e o menor foi: {menor_numero}")