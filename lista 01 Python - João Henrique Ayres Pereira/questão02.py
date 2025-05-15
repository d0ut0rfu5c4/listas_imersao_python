print(" 2) peça ao usuário para inserir o valor original de um produto e a porcentagem de desconto. Calcule e mostre o valor do produto após o desconto")

def Calcular_desconto():
    valor_entrada = float(input("Digite o valor original do produto: "))
    valor_desconto = float(input("Digite o valor do desconto: "))
    valor_final = valor_entrada - (valor_entrada * valor_desconto/100)

    print("O valor do desconto é: R$",valor_final)

Calcular_desconto()

print()