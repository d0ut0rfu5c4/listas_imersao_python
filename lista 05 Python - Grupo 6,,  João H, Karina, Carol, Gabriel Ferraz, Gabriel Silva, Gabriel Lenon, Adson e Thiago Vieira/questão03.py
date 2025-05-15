def criar_senha(dia, mes, ano):
    mes_invertido = mes[::-1]  # o mês invertido
    dia_invertido = dia[::-1]  # o dia invertido
    ano_invertido = ano[::-1] # ano invertido
    
    senha = f"{mes}$" \
            f"{dia_invertido}#" \
            f"{dia}!" \
            f"{mes_invertido}*" \
            f"{ano_invertido}*" \
    
    return senha

# qual e a data de nascimento do usuário
dia = input("Digite o dia de nascimento (dd): ")
mes = input("Digite o mês de nascimento (mm): ")
ano = input("Digite o ano de nascimento (aaaa): ")

# Mostre a senha que foi gerada
print(f"Sua senha é: {criar_senha(dia, mes, ano)}")