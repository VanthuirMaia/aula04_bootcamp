# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros: dict = {
    "Livro_01": {
        "Titulo": "Deixe de ser Probre",
        "Autor": "Eduardo Fieldberg",
        "Ano": "2022",
    },
    "Livro_02": {"Titulo": "Pega a Visão", "Autor": "Rick Chester", "Ano": "2018"},
    "Livro_03": {
        "Titulo": "Pai Rico, Pai Pobre",
        "Autor": "Robert Kiyosaki",
        "Ano": "2000",
    },
}

# Mostra todos os livros do Dicionário
for chave, detalhes in livros.items():  # Itera sobre cada Dicionário
    for campo, valor in detalhes.items():  # Itera sobre os itens do dicionario
        print(f" {campo}: {valor}")  # Mostra os valores
    print()  # Linha em branco para separar os dicionarios

# Mostra um livro específico, de acordo o nome do Dicionário
livro_escolhido = "Livro_02"

if (
    livro_escolhido in livros
):  # Condicional para verificar se o livro escolhido esta no Dicionário
    for campo, valor in livros[livro_escolhido].items():  # Itera sobre o Dicionário
        print(f"{campo}: {valor}")  # Mostra o valor
else:
    print("Livro não encontrado.")  # Caso a condição seja negativa
