# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1:dict = {"a": 1, "b": 2}
dicionario2:dict = {"c": 3, "d": 4}

fusao:dict = {**dicionario1, **dicionario2}

print(fusao)