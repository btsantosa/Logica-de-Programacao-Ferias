# Estudo de Caso 3: Ajuste de Hidratação Diária
# Contexto: Um app de saúde ajusta registros de água consumida 
# para garantir o mínimo diário de 2.0 litros (20 decilitros). 
# Cada incremento adiciona 1 decilitro (0.1L).
# Registros originais: [15, 20, 18, 25, 19, 17] (em decilitros). 



def ajustar_agua(agua, minimo):
    for i in range(6):
        while agua[i] < minimo:
            agua[i] = agua[i] + 1
            if agua[i] > minimo:
                agua[i] = minimo
    return

registros_originais = [15, 20, 18, 25, 19, 17]
minimo_diario = 20

print("Consumo de água atual em decilitros: ")
for i in registros_originais:
    print(i)

ajustar_agua(registros_originais, minimo_diario)

print ("Consumo de água atualizado em decilitros: ")
for i in registros_originais:
    print(i)