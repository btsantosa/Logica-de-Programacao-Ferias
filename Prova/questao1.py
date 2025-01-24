# Escreva um programa que execute as seguintes etapas:
# Solicite ao usuário que informe o consumo de energia de cada um
# dos 6 apartamentos, em quilowatt-hora (kWh), não permitindo inserir números negativos.

# Calcule o consumo total do condomínio somando o consumo de todos os apartamentos.
# Calcule a média de consumo dos 6 apartamentos.
# Ao final, o programa deve exibir:

# O consumo total do condomínio em kWh. OK
# O número de apartamentos que consumiram mais que a média.
# O número de apartamentos que consumiram menos que a média.
# O apartamento com o maior consumo e seu valor de consumo. OK
# O apartamento com o menor consumo e seu valor de consumo. OK

contador = 0
somaApartamento = 0
maior = 1
apartamentosMaiorConsumo = 0
apartamentosMenosConsumo = 0
apartamentoMenor = 0
menor = 0

while True: 
        apartamentoMaior = 1

        for i in range(4):
            
            apartamento = int(input(f"Digite o consumo do apartamento {i}: "))
      
            contador += 1
            # Soma
            somaApartamento += apartamento
            # Média 
            mediaApartamento = somaApartamento / contador

            # Descobrir valor que consumiu mais
            if apartamento > maior:
                maior = apartamento
                apartamentoMaior = i + 1

            # Descobrir valor que consumiu menos
            if apartamento < menor:
                menor = apartamento
                apartamentoMenor = i + 1

            # Numero de apartamentos que mais consumiu
            if apartamento > mediaApartamento:
                apartamentosMaiorConsumo = i + 1

            # Numero de apartamentos que menos consumiu
            if apartamento < mediaApartamento:
                apartamentosMenosConsumo = i + 1
                
        
        print(f"A soma do KWh dos 4 apartamentos é: {somaApartamento}")
        print(f"A média de consumo dos 4 apartamentos é: {mediaApartamento}")
        print(f"O apartamento que mais consumiu foi: {apartamentoMaior} com {maior} KWh")
        print(f"O apartamento que menos consumiu foi: {apartamentoMenor} com {menor} KWh")
        print(f"Apartamentos que consumiram maior que a média {apartamentosMaiorConsumo}")
        print(f"Apartamentos que consumiram menor que a média {apartamentosMenosConsumo}")
        break  
        
        

