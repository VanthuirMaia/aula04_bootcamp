# Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.


def reverter(palavra):
    return palavra[::-1]


palavra = input("Digite a palavra: ")
resultado = reverter(palavra)

print(resultado)
