# Estudo de Caso 1: Controle de Estoque em um Armazém
# Contexto: Um sistema atualiza o estoque de produtos para garantir 
# que nenhum item fique abaixo do nível mínimo de 50 unidades. 
# A função atualizar_estoque incrementa unidades até atingir o mínimo.
# Lista original: estoque = [45, 55, 40, 60, 38, 50], minimo = 50.

# O item do FOR tem que ficar dentro do colchetes do item do DEF

def atualizar_estoque(item, limite):
    for itens in range(6):
        while item[itens] < limite:
            item[itens] = item[itens] + 1
    return
        
estoque = [45, 55, 40, 60, 38, 50]
minimo = 50

print("Estoque atual: ")
for i in estoque:
    print(i)

atualizar_estoque(estoque, minimo)

print ("Estoque atualizado")
for i in estoque:
    print(i)