# Escreva um programa que solicite ao usuário a entrada de números inteiros, um de cada vez. 
# O programa deve continuar solicitando números até que o usuário insira o número 0. 
# Após o término, exiba:
# A média de todos os números positivos digitados (excluindo o 0).
# O maior número digitado.

media = 0
contador = 0
somaNumero = 0

while True:

    numero = int(input("Insira um número: (0 para sair)"))

    

    if numero == 0:
        print("OK")
        break

    contador += 1
    somaNumero += numero

#calculo media
if contador > 0:
    media = somaNumero / contador
else:
    media = 0

print(f"A media é {media}")
print(f"O programa executou o codigo {contador} vezes")
