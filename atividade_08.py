# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas:list = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20},
    {"nome": "Arthur", "idade": 50},
    {"nome": "Valter", "idade": 25},
    {"nome": "Wanderley", "idade": 24}
]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["nome"])

print(pessoas_ordenadas)