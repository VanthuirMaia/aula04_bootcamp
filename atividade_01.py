from typing import Dict, Any

livro: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "João da Silva",
    "Ano_Publ": 2005
}

lista_de_elementos: list = livro.items()
for elemento in lista_de_elementos:
    print(elemento)

