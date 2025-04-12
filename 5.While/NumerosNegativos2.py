# Escreva um programa em Python que solicite ao usuário números inteiros positivos, 
# um de cada vez. O programa deve parar quando o usuário inserir um número negativo.

# Após o término do programa, exiba:

# A quantidade de números positivos digitados.
# A soma de todos os números positivos digitados.
# A média dos números positivos digitados (caso nenhum número positivo tenha sido digitado,
#  exiba a média como 0).

contagem = 0
somaNumeros = 0

while True:

    numero = int(input("Escreva um número (negativo para sair)"))

    if numero < 0:
        print("OK")
        break

    contagem += 1
    somaNumeros += numero

if numero <= 0:
    media = somaNumeros / contagem
else:
    media = 0

print(f"Os numeros positivos digitados é {contagem}")
print(f"A soma dos números é {somaNumeros}")
print(f"A média é {media}")
