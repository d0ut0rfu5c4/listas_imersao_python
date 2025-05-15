# 7) Escreva um programa que leia o custo de produção de um produto e seu preço de venda.
# Calcule e mostre o lucro bruto obtido na venda do produto.

def Calculo_lucro_bruto():
    custo_producao = float(input("Informe o custo do produto: "))
    preco_venda = float(input("Informe agora o preço de venda do produto: "))
    calculoLucro = preco_venda - custo_producao
    print("O Lucro bruto será de: R$", calculoLucro)

Calculo_lucro_bruto()

print()