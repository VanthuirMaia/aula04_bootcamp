# Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def encontrar_pares(lista, soma):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == soma:
                pares.append((lista[i], lista[j]))
    return pares


numeros = [1, 2, 3, 4, 5, 6]
numero_soma = 7
resultado = encontrar_pares(numeros, numero_soma)
print(f"Os pares que somam {numero_soma} são: {resultado}")
