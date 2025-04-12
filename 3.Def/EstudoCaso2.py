# Questão 02: Um banco deseja implementar um sistema básico de caixa eletrônico. 
# O sistema deve permitir que o cliente realize depósitos, saques e consulte o 
# saldo da conta. Todas as operações devem ser realizadas utilizando funções 
# para organizar o código.


# Problema:
# Crie um programa que:
# Permita ao usuário depositar um valor na conta.
# Realize saques (desde que o saldo seja suficiente).

# Consulte o saldo da conta.
# Use funções (def) para organizar as operações do sistema.

# Requisitos:
# As funções devem ser utilizadas para:
# Depositar valores.
# Realizar saques.
# Consultar o saldo.
# Deve validar entradas e garantir que o saldo nunca fique negativo.



def depositar(saldo, valor):          
    saldo += valor
    return saldo

def sacar (saldo, valor):
    saldo -= valor
    return saldo

saldo_conta = 0

while True:
    print()
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver saldo")
    print("4. Para sair")

    opcao = input("Selecione uma das opções: ")

    if opcao == "1":
        deposito = int(input("Digite o valor inteiro para depositar: "))
        saldo_conta = depositar(saldo_conta, deposito)

    elif opcao == "2":
        saque = int(input("Digite o valor inteiro para sacar: "))        
        if saldo_conta < saque:
            print("Não tem saldo na conta suficiente para saque")
        else:
            saldo_conta = sacar(saldo_conta, saque)


    elif opcao =="3":
        print(f"O seu saldo é {saldo_conta}")

    elif opcao == "4":
        break



    


