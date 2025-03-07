# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# Minha Solução:
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares: list = []
impares: list = []

for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Os números pares são: {pares}")
print(f"Os números Ímpares são: {impares}")


# Jornada de Dados
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)
