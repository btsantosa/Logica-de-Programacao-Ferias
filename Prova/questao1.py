# Escreva um programa que execute as seguintes etapas:
# Solicite ao usuário que informe o consumo de energia de cada um
# dos 6 apartamentos, em quilowatt-hora (kWh), não permitindo inserir números negativos.

# Calcule o consumo total do condomínio somando o consumo de todos os apartamentos.
# Calcule a média de consumo dos 6 apartamentos.
# Ao final, o programa deve exibir:

# O consumo total do condomínio em kWh.
# O número de apartamentos que consumiram mais que a média.
# O número de apartamentos que consumiram menos que a média.
# O apartamento com o maior consumo e seu valor de consumo.
# O apartamento com o menor consumo e seu valor de consumo.]

contador = 0
somaApartamento = 0

while True: 
        maior = int(input(f"Digite o consumo do apartamento 1: "))
        apartamentoMaior = 1

        for i in range(3):
            apartamento = int(input(f"Digite o consumo do apartamento {i + 2}: "))
      
            contador += 1
            # Soma
            somaApartamento += apartamento
            # Média 
            mediaApartamento = somaApartamento / contador

            # Descobrir valor que consumiu mais
            if apartamento > maior:
                maior = apartamento
                apartamentoMaior = i + 2
        
            if apartamento < maior:
                menor = apartamento
                apartamentoMenor = i + 2
            # Descobrir valor que consumiu mais
            
        print(f"A soma do KWh dos 6 apartamentos é: {somaApartamento}")
        print(f"A média de consumo dos 6 apartamentos é: {mediaApartamento}")
        print(f"O apartamento que mais consumiu foi: {apartamentoMaior} com {maior} KWh")
        print(f"O apartamento que menos consumiu foi: {apartamentoMenor} com {menor} KWh")
        break  
        
        

