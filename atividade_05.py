# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# Lista de itens
frutas: list = ["maçã", "banana", "cereja"]

# Dicionário com preços
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# Calculando o preço total
preco_total = sum(precos[item] for item in frutas)

# Exibindo o resultado
print(f"O preço total da lista de compras é R${preco_total:.2f}")
