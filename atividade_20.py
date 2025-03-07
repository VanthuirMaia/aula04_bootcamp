# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas


def ordenar_chaves(dicionario):
    return sorted(dicionario.keys())


dados = {"banana": 3, "maçã": 5, "laranja": 2, "uva": 4}
resultado = ordenar_chaves(dados)
print(resultado)
