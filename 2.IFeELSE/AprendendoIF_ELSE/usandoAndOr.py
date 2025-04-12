# Nesse caso depende da ordem

idade = 24
possui_cartao = False

# A compparação de idade vem primeiro, se idade é 24, mas não possui cartão, então é False
# A idade é maior que 18, então é True
# or é um ou outro, se um for true, então é igual a true, ou seja: False or True = True

if (idade >= 18 and possui_cartao) or idade >= 21:
    print("Você pode fazer compras com desconto.")
else:
    print("Você não pode fazer compras com desconto.")