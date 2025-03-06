# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# Minha solução
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

id_produto = 1 # Você escolhe o ID que quer alterar
novo_preco = 250 # Novo preço

for produto in produtos:
    if produto["id"] == id_produto:
        produto["preço"] = novo_preco
        print(f"O preço do produto {produto['nome']} foi alterado para R${produto['preço']:.2f}.")
        break

print(produtos)


# Jornada de dados
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)