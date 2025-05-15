print("4) Peça ao usuário para inserir um valor inicial, a taxa de juro e o tempo. Calcule e mostre o valor futuro após o período especificado com juros simples.")

print()

#fómula para calcular o juros simples:
# juros = Capital * taxa * T

valor_inicial = float(input("inisira o valor inicial: "))
taxa_juros = float(input("informe a taxa de juros; "))
tempo = int(input("digite o tempo que deseja: "))

taxa_juros = taxa_juros/100

juros = valor_inicial * taxa_juros * tempo
print("Valor futuro: R$",juros + valor_inicial)

print()
