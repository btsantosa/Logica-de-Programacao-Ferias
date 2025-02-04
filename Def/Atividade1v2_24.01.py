# Desenvolva um programa que simule a geração de 4 notas aleatórias no formato decimal 
# (float), com valores entre 0.0 e 10.0. O programa deve exibir as notas geradas e apresentar, 
# de forma organizada, os seguintes cálculos:
# Média das notas
# Soma das notas
# Maior nota
# Menor nota
# Para isso, implemente funções específicas para cada cálculo 
# (média, soma, maior nota e menor nota) e utilize-as no programa principal.

def depositar(saldo, valor):
    saldo += valor  # Acumula o valor ao saldo
    return saldo  # Retorna o novo saldo

saldo = 0  # Saldo inicial

while True:
    print("\n1. Depositar")
    print("2. Sacar")
    print("3. Ver saldo")
    print("4. Sair")

    opcao = input("Selecione uma das opções: ")

    if opcao == "1":
        valor = int(input("Digite o valor do depósito: "))
        saldo = depositar(saldo, valor)  # Atualiza o saldo com o retorno da função
        print(f"Depósito realizado! Novo saldo: {saldo}")

    elif opcao == "3":
        print(f"Seu saldo atual é: {saldo}")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")




