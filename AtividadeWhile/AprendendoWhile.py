# O while é uma estrutura de controle de fluxo em Python que permite criar loops 
# (ou laços) baseados em uma condição. 
# O bloco de código dentro do while é repetido enquanto a condição 
# especificada for avaliada como verdadeira (True).
# Aqui está uma estrutura básica do while:

numero = float(input("Digite um número: "))

while True:

  if numero % 2 == 0:
    print("Fim do Programa")
    break
  else:
    numero = float(input("Digite um número: "))
