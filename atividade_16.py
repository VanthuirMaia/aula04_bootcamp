# Escreva uma função que receba uma lista de números e retorne a soma de todos os números.


def somar_numeros(lista):
    return sum(lista)


numeros: list = [10, 20, 30, 40, 50]

resultado = somar_numeros(numeros)
print(f"A soma dos números é: {resultado}")
