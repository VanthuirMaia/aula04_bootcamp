# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# Solicita a entrada do usuário
texto = input("Digite uma string: ")

# Dicionário para armazenar a contagem de caracteres
contagem = {}

# Itera sobre cada caractere na string
for caractere in texto:
    contagem[caractere] = contagem.get(caractere, 0) + 1

# Ordena do maior para o menor número de ocorrências
contagem_ordenada = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

# Exibe o resultado
print("\nContagem de caracteres (ordenada do maior para o menor):")
for caractere, count in contagem_ordenada:
    print(f"'{caractere}': {count}")


# Outra opção
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem


print(contar_caracteres("engenharia de dados"))
