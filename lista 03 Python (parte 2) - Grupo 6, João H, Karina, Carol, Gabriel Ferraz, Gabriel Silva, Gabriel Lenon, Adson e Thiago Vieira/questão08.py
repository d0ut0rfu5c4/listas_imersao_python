# feito por Carol Sousa

#questao 8
# Solicitar a quantidade de clientes
num_clientes = int(input("Quantos clientes há na loja? \n"))
# Inicializar variáveis
clientes_aptos = 0
total_bonus = 0.0

# Loop para coletar dados de cada cliente
for _ in range(num_clientes):
    nome = input("Digite o nome do cliente: \n")
    valor_compras = float(input(f"Digite o valor total das compras de {nome} no ano (R$): \n"))
    
    # Verificar se o cliente é apto para o bônus
    if valor_compras >= 2000:
        bonus = valor_compras * 0.15  # Cálculo do bônus de 15%
        print(f"{nome} - Cliente apto para receber o bônus de R$ {bonus:.2f}\n")
        
        # Atualizar contagem de clientes aptos e o total de bônus
        clientes_aptos += 1
        total_bonus += bonus
    else:
        print(f"{nome} - Cliente não apto para receber o bônus.\n")

# Exibir resultados finais
print(f"\nTotal de clientes que ganharam o bônus: {clientes_aptos}\n")
print(f"Total em bônus a ser pago: R$ {total_bonus:.2f}\n")