#10) Peça ao usuário para inserir o valor total de uma compra e o número de parcelas desejadas.
# Calcule e mostre o valor de cada parcela, considerando que não há juros.

def Calcule_valor_parcela():
    valor_total_compra = float(input("Por favor, insira o valor da compra: "))
    qtd_parcelas = int(input("quantas parcelas você gostaria de efetuar o pagamento: "))
    valor_parcela = valor_total_compra/qtd_parcelas

    print("Valor de cada parcela: R$", valor_parcela)

Calcule_valor_parcela()
