# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades: list = [22, 15, 30, 17, 18]

maior_idade: list = []

for item in idades:
    if item >= 18:
        maior_idade.append(item)

maior_idade_ordenada = sorted(maior_idade)

print(maior_idade)
print(maior_idade_ordenada)


# Opção da Jornada de Dados
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)
