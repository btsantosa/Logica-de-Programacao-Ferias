# Faça um Programa que peça dois números e imprima o maior deles.

valorA = int(input("Digite o valor A: "))
valorB = int(input("Digite o valor B: "))

if valorA > valorB:
    print(f"O maior valor é: {valorA}")
elif valorB > valorA:
    print(f"O maior valor é: {valorB}")