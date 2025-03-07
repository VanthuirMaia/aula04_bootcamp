# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {
    "Teclado": 10,
    "Mouse": 0,
    "Monitor": 3,
    "CPU": 0,
    "Fonte": 2,
    "Processador": 5,
    "Placa Mãe": -2,
}

estoque_disponivel = {
    produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0
}
estoque_critico = {
    produto: quantidade
    for produto, quantidade in estoque.items()
    if quantidade <= 2 and quantidade > 0
}
estoque_indisponivel = {
    produto: quantidade for produto, quantidade in estoque.items() if quantidade < 1
}


print(f"Os produtos com estoque disponível são: {estoque_disponivel}")
print(f"Ja os produtos com estoque critico são: {estoque_critico}")
print(f"E os produtos com estoque zerado e/ou negativo são: {estoque_indisponivel}")
