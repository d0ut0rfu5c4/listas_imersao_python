'''7 ) Uma operadora de telefonia móvel deseja oferecer planos personalizados para seus
clientes. Eles oferecem três tipos de planos com diferentes franquias de minutos e
internet:
● Plano Básico: 100 minutos e 5GB de internet por R$ 50.
● Plano Intermediário: 300 minutos e 10GB de internet por R$ 80.
● Plano Avançado: 500 minutos e 20GB de internet por R$ 120.
Caso o cliente ultrapasse a franquia de minutos, será cobrado R$ 1 por minuto
adicional. Se ultrapassar a franquia de internet, será cobrado R$ 10 por GB adicional.
Escreva um programa que peça ao usuário para escolher um plano, informar quantos
minutos e quantos GB ele utilizou no mês. O programa deve calcular e mostrar o valor
total da fatura.'''

def fatura_internet():
    print("\n Planos disponíveis: ")
    print("\n 1 - Básico: 100 min, 5GB por R$ 50 \n")
    print("\n 2 - Intermediário: 300 min, 10GB por R$ 80 \n")
    print("\n 3 - Avançado: 500 min, 20GB por R$ 120 \n")

# Entrada do usuário
plano = int(input("\n Escolha o plano (1, 2 ou 3): "))
minutos_usados = int(input("\n Informe a quantidade de minutos utilizados: "))
internet_usada = float(input("\n Informe a quantidade de GB utilizados: "))

# Dicionário com as informações dos planos
planos = {
    1: {"nome": "Básico", "minutos": 100, "internet": 5, "preco": 50},
    2: {"nome": "Intermediário", "minutos": 300, "internet": 10, "preco": 80},
    3: {"nome": "Avançado", "minutos": 500, "internet": 20, "preco": 120}
}

# Verifica se o plano é válido e calcula a fatura
if plano in planos:
    plano_selecionado = planos[plano]
    custo_adicional_minutos = max(0, minutos_usados - plano_selecionado["minutos"]) * 1
    custo_adicional_internet = max(0, internet_usada - plano_selecionado["internet"]) * 10
    total = plano_selecionado["preco"] + custo_adicional_minutos + custo_adicional_internet
    print(f"\n Valor da fatura: R$ {total:.2f}")
else:
    print("\n Opção inválida de plano.")

fatura_internet()