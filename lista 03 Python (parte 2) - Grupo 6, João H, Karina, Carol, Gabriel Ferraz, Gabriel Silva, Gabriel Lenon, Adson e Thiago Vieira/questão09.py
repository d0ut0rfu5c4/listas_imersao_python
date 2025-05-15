# feito por Gabriel Silva

#Exercício 09:

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

vendas = []

for i in meses:

    valor = float(input(f"\nDigite o valor de vendas para o mês de {i}:\n"))
    vendas.append(valor)


maior_venda = max(vendas)
menor_venda = min(vendas)
media_vendas = sum(vendas) / len(vendas)
total_vendas = sum(vendas)

mes_maior_venda = meses[vendas.index(maior_venda)]
mes_menor_venda = meses[vendas.index(menor_venda)]

# Exibição dos resultados
print("\nResultados da Análise de Vendas:\n")
print(f"Mês com maior venda: {mes_maior_venda} - R$ {maior_venda:.2f}")
print(f"Mês com menor venda: {mes_menor_venda} - R$ {menor_venda:.2f}")
print(f"Média de vendas no ano: R$ {media_vendas:.2f}")
print(f"Total de vendas no ano: R$ {total_vendas:.2f}")

