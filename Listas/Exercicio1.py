# Uma escola precisa de um sistema simples para gerenciar as notas dos alunos em uma turma.
# Cada aluno tem uma lista de notas, e o objetivo é verificar se algum aluno precisa de
# recuperação, ou seja, se alguma nota está abaixo da média exigida (6.0). Caso a nota esteja
# abaixo, o sistema deve aumentar a nota em 1 ponto, desde que não ultrapasse 6.0, simulando
# uma atividade de recuperação.

def atualizar_notas(nota):
    for nota in range(4):
        while notas[nota] < 6:
            notas[nota] = notas[nota] + 1
    return

notas = [2, 5, 7, 9]  

print("Notas Originais")
for i in notas:
    print(i)
        

print("Notas Atualizadas")

atualizar_notas(notas)
for i in notas:
    print(i)

