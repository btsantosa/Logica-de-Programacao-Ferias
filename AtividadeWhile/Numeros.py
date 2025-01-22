# Solicite ao usuário que insira dois números. O programa continuará a executar 
# até que o segundo número seja pelo menos duas vezes maior que o primeiro. Ao final, 
# o programa exibirá a quantidade de repetições realizadas durante a execução.
contador = 0

while True:

    numero1 = int(input("Insira um número: "))
    numero2 = int(input("Insira outro número: "))

    contador += 1

    if numero2 >= numero1 * 2:
        print("OK")
        break
    else:
        print("O segundo número precisa ser duas vezes maior que o primeiro")
       

print(f"O programa executou o codigo {contador} vezes")
