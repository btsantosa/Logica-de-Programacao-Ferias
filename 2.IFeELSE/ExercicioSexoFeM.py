# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite 'F' para Feminino e 'M' para Masculino: ")

if sexo == "F":
    print ("Seu gênero é feminino")
elif sexo == "M":
    print("Seu genero é masculino")
else:
    print("Sexo Inválido")