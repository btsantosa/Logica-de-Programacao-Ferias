# Crie um função para gerar numeros aleatorio e o usuario ira escolher o numero inicial e final do sorteio
import  random

def gerador (a, b):
   return random.randint(a, b)
   

numero1 = int(input("Digite o número inicial: "))
numero2 = int(input("Digite o número final: "))


resultado_gerador = gerador(numero1, numero2)
print(resultado_gerador)

print(f"O numero aleatorio gerado entre {numero1} e {numero2} é {resultado_gerador}")