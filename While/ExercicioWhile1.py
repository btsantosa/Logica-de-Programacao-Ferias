# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.

while True:

    nota = int(input("Escreva uma nota entre 0 e 10: "))

    if nota > 10 or nota < 0:
        print("Valor inválido")
    else:
        print(f"O valor que você digitou é {nota}")
        break
