# 5) Um hotel de luxo deseja automatizar seu sistema de reservas. Eles possuem três tipos de
# suítes: Standard, Luxo e Presidencial. Cada tipo de suíte tem uma quantidade limitada
# de noites que pode ser reservada a um preço diferente. O hotel definiu as seguintes
# regras:
# 1. Suíte Standard: Custa R$ 250 por noite, limite de 15 noites.
# 2. Suíte Luxo: Custa R$ 500 por noite, limite de 10 noites.
# 3. Suíte Presidencial: Custa R$ 1200 por noite, limite de 7 noites.
# Além disso, se o cliente desejar ficar 5 noites ou mais, ele recebe um desconto de 10%
# no valor total, independentemente do tipo de suíte escolhida. Escreva um programa que
# peça ao usuário para escolher o tipo de suíte, a quantidade de noites e informe o valor
# total da estadia. Se a quantidade de noites informada for maior que o limite disponível,
# informe ao usuário e finalize o sistema.

print("Tipos de Suíte:")
print("1 - Standard (R$ 250/noite, máximo 15 noites)")
print("2 - Luxo (R$ 500/noite, máximo 10 noites)")
print("3 - Presidencial (R$ 1200/noite, máximo 7 noites)")

tipo_suite = int(input("Escolha o tipo de suíte (1, 2 ou 3): "))
noites = int(input("Digite a quantidade de noites desejadas: "))

suites = {
    1: {"nome": "Standard", "preco": 250, "limite": 15},
    2: {"nome": "Luxo", "preco": 500, "limite": 10},
    3: {"nome": "Presidencial", "preco": 1200, "limite": 7}
}

if tipo_suite in suites:
    suite = suites[tipo_suite]
    if noites > suite["limite"]:
        print("Quantidade de noites excede o limite disponível para essa suíte.")
    else:
        total = noites * suite["preco"]
        if noites >= 5:
            total *= 0.9  # Aplicando desconto de 10%
        print(f"Valor total da estadia: R$ {total:.2f}")
else:
    print("Opção inválida de suíte.")