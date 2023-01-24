# strings e input

# strings são criadas com aspas duplas ou simples
a = "isto é uma string"  # formatador altera para aspas duplas automaticamente
b = "isto também é uma string"

print(f"{a}, {b}")

# variáveis
def babadi():
    nome = "Victor"
    sobrenome = "Vernasqui"
    print(f"{nome} {sobrenome}")


# user input
nome = input("Digite seu nome: ")
idade = input("digite sua idade: ")
print(f"seu nome é {nome} e idade é {idade}?")
