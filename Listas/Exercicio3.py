# Estudo de Caso 2: Controle de Temperatura em uma Estufa
# Contexto: Um termostato ajusta a temperatura de ambientes para não 
# ficar abaixo de 20°C. A função incrementa 1°C por iteração até atingir o mínimo.
# Temperaturas originais: [18.5, 20.0, 19.0, 22.5, 17.0, 19.9].



def ajustar_temperatura(temp, ideal):
    for i in range(6):
        while temp[i] < ideal:
            temp[i] = temp[i] + 1
            if temp[i] > ideal:
                temp[i] = ideal
    return

temperaturas_originais = [18.5, 20.0, 19.0, 22.5, 17.0, 19.9]
temperatura_ideal = 20.0    

print("Temperatura atual: ")
for i in temperaturas_originais:
    print(f"{i}")

ajustar_temperatura(temperaturas_originais, temperatura_ideal)

print ("Temperatura ajustada: ")
for i in temperaturas_originais:
    print(f"{i}")
