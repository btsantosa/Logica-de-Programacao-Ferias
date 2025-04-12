# Faça um programa que leia 5 números e informe o maior número.

print("Digite 5 números: ")

maior = int(input(f"Digite o número 1: "))

for i in range(4):
    numero = int(input(f"Digite o número {i + 2}: "))

    if numero > maior:
        maior = numero

print (maior)
    
    