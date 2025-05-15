# 9) Peça ao usuário para inserir o valor de um produto e a taxa de imposto aplicada sobre ele.
#Calcule e mostre o valor final do produto com o imposto.

def Calcular_produto_imposto():
    valor_do_produto = float(input("Informe o valor do produto: "))
    taxa_de_imposto = float(input("Informe a taxa de imposto do respectivo produto: "))
    valor_final = valor_do_produto + valor_do_produto * taxa_de_imposto/100
    print("Valor final do produto com Imposto: R$ ", valor_final)

Calcular_produto_imposto()

print()