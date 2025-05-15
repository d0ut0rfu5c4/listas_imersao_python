# 5) QUESTÃO 5: Escreva um programa que leia o valor total das vendas de um vendedor e a porcentagem de
# comissão que ele recebe. Calcule e mostre o valor da comissão.
print()

valor_total_vendas = float(input("Digite o valor total de vendas: "))
porcentagem_comissao = float(input("Digite o valor da comissão: "))

porcentagem_comissao = porcentagem_comissao/100
valor_comissao = valor_total_vendas * porcentagem_comissao

print("O valor de comissão é: R$",valor_comissao)
