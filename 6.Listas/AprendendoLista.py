# Uma lista é uma coleção ordenada de elementos, onde cada elemento pode ser de qualquer tipo de dado. 
# Em Python, listas são usadas para armazenar múltiplos itens em uma única variável.

# ADICIONAR

# 1. append() → adiciona no final:
# frutas.append("laranja")

# 2. insert(posição, valor) → adiciona em uma posição específica:
# frutas.insert(1, "abacaxi")  # insere "abacaxi" na posição 1

# REMOVER

# 1. remove(valor) → remove o primeiro valor igual ao informado:
# frutas.remove("banana")

# 2. pop() → remove o último item (ou o da posição que você quiser):
# frutas.pop()        # remove o último
# frutas.pop(0)       # remove o primeiro

# 3. del → deleta usando o índice:
# del frutas[1]       # remove o item da posição 1

# MODIFICAR

# Você acessa pela posição (índice começa no 0):
# frutas[0] = "pera"  # substitui "maçã" por "pera"

# PESQUISAR

# 1. Usando in:
# if "uva" in frutas:
#     print("Tem uva na lista!")

# 2. Encontrar o índice com index():
# posicao = frutas.index("uva")  # retorna a posição da "uva"