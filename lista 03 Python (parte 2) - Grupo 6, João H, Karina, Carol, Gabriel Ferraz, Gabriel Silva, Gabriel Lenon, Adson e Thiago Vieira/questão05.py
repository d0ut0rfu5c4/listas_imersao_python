# feito por Karina Meirles Varela

pessoas = []

# lendo dados 5 pessoas
for i in range(5):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    pessoas.append((nome, idade, altura))

# achando a pessoa mais alta
pessoa_mais_alta = max(pessoas, key=lambda x: x[2])

# resultado
nome, idade, altura = pessoa_mais_alta
print(f"{nome}, com {idade} anos e {altura:.2f}m, é a pessoa mais alta do grupo.")