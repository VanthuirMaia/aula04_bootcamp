# Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def numero_primo(numero):
    if numero < 2:
        print(f"O número {numero} não é primo")
        return
    
    is_primo = True
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            is_primo = False
            print(f"O número {numero} não é primo (divisível por {i})")
            break
    
    if is_primo:
        print(f"O número {numero} é primo")

# Exemplo de uso:
numero = int(input("Digite um número: "))
numero_primo(numero)



