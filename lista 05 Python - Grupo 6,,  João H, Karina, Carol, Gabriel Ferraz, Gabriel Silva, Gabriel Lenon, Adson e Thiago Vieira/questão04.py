def editar_data_nascimento(data):
    meses = {
        "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
        "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
        "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
    }
    
    dia, mes, ano = data.split('/')
    mes_extenso = meses.get(mes, "Mês inválido")
    
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

print(editar_data_nascimento(data_nascimento))