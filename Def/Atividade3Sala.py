import  random

def gerador (a, b):
   return random.randint(a, b)
   

numero1 = int(input("Digite o número inicial: "))
numero2 = int(input("Digite o número final: "))


resultado_gerador1 = gerador(numero1, numero2)
resultado_gerador2 = gerador(numero1, numero2)

print(f"O numero aleatorio gerado entre {numero1} e {numero2} é {resultado_gerador1}")
print(f"O numero aleatorio gerado entre {numero1} e {numero2} é {resultado_gerador2}")
