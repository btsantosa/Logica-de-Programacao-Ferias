# Você é responsável por criar um verificador de acesso para um evento. 
# Os critérios de acesso são os seguintes: 
# - A pessoa deve ter pelo menos 18 anos de idade para entrar.
# - Caso a pessoa tenha entre 16 e 17 anos, ela pode entrar se estiver acompanhada por 
# um adulto que tenha pelo menos 18 anos.
# - Pessoas com menos de 16 anos não podem entrar.

idade = 18
idadeadulto = 18

idade = int((input("Quual sua idade?: ")))

if idade >= 18:
    print ("Pode passar")
elif idade == 17 or idade == 16:
    print("16 e 17 anos de idade só passa com adulto")

    if idade == 17 or idade == 16:
        idadeadulto = int(input("Qual a idade do adulto?: "))

        if idadeadulto >= 18:
            print("Pode passar")
        elif idadeadulto == 17 or idadeadulto == 16:
            print("16 e 17 anos de idade só passa com adulto")
else:
    print("não pode passar")

    