# 1) 1) Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e mostre uma
# mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado). Mostre uma
# mensagem de erro, se necessário.
# Entrada Saída

merital_status = input('"Defina seu estado civil, digite c par casado, s para solteiro, v para viuvo, d  para divorciado ou u para união estável: ')

if merital_status == 's' or merital_status == 'S':
    print("\n Solteiro(a)")
elif merital_status == 'c' or merital_status == 'C':
    print("\n Casado(a)")
elif merital_status == 'v' or merital_status == 'V':
    print("\n Viuvo(a)")
elif merital_status == 'd' or merital_status == 'D':
    print("\n Divorciado(a)")
elif merital_status == "u" or merital_status == 'U':
    print("União estável")
else:
    print("Valor inválido!")


