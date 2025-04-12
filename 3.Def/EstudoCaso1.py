# Desenvolva um programa que simule a geração de 4 notas aleatórias no formato decimal 
# (float), com valores entre 0.0 e 10.0. O programa deve exibir as notas geradas e apresentar, 
# de forma organizada, os seguintes cálculos:
# Média das notas
# Soma das notas
# Maior nota
# Menor nota
# Para isso, implemente funções específicas para cada cálculo 
# (média, soma, maior nota e menor nota) e utilize-as no programa principal.

import random
resultadoSoma = 0
resultadoMedia = 0
nMenor = 0
nMaior = 0

n1 = random.uniform(0.0, 10.0)
n2 = random.uniform(0.0, 10.0)
n3 = random.uniform(0.0, 10.0)
n4 = random.uniform(0.0, 10.0)

def soma (a, b, c, d):
    resulSoma = a + b + c + d
    return resulSoma  

def media(a, b, c, d):
    resulMedia = (a + b + c + d) / 4
    return resulMedia

def maior(a, b, c, d):
    notaMaior = a
    if b > notaMaior:
        notaMaior = b
    elif c > notaMaior:
        notaMaior = c
    elif d > notaMaior:
        notaMaior = d
    return notaMaior
    
def menor(a, b, c, d):
    notaMenor = a
    if b < notaMenor:
        notaMenor = b
    elif c < notaMenor:
        notaMenor = c
    elif d < notaMenor:
        notaMenor = d
    return notaMenor
    
nMenor = menor(n1, n2, n3, n4)
nMaior = maior(n1, n2, n3, n4)
resultadoSoma = soma(n1, n2, n3, n4)
resultadoMedia = media(n1, n2, n3, n4)

print(f"A nota 1 é: {n1:.2f}")
print(f"A nota 2 é: {n2:.2f}")
print(f"A nota 3 é: {n3:.2f}")
print(f"A nota 4 é: {n4:.2f}")

print(f"O resultado da soma é: {round(resultadoSoma, 2)}")
print(f"O resultado da média é: {round(resultadoMedia, 2)}")
print(f"A nota menor é: {nMenor:.2f}")
print(f"A nota maior é: {nMaior:.2f}")
