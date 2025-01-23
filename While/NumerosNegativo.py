# Escreva um programa que solicite ao usuário a entrada de números inteiros, um de cada vez. 
# O programa deve continuar solicitando números até que o usuário insira um número negativo. 
# Após o término, exiba:
# A quantidade total de números digitados (excluindo o número negativo).
# A soma de todos os números positivos digitados.

contador = 0
somaNumeros = 0
while True:

    numero1 = int(input("Insira um número: "))

    contador += 1
    somaNumeros += numero1

    if numero1 < 0:
        print("OK")
        break
    else:
        print("Os numeros precisam ser negativos")

print(f"O programa executou o codigo {contador} vezes")
print(f"O programa somou {somaNumeros} vezes")
