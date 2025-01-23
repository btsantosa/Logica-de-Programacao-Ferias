import random

def aleatorio():
# Gerar um numero decimal entre 1.5 e 5.5 # numero = random.uniform(1.5, 5.5)

    return random.randint(0, 100)

numero_gerado = aleatorio()
print(numero_gerado)