# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = input("Digite sua String: ")

frequencia = {}

for caractere in texto:
    frequencia[caractere] = frequencia.get(caractere, 0) + 1

frequencia_ordenada = dict(
    sorted(frequencia.items(), key=lambda item: item[1], reverse=True)
)

print(frequencia)
print(frequencia_ordenada)
