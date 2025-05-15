# questão  feita por João Henriue Ayres Pereira

'''1 ) Faça um algoritmo que leia idades até o usuário digitar -1. O programa deve exibir o
total de idades válidas digitadas, a média das idades, quantas são maiores ou igual a 25
e quantas são menores que 25.'''

total_idades = 0 # esta variável irá receber a quantidade total de idades que o usuário informar
soma_idades = 0 # esta variável irá fazer a soma das idades para posteriormente fazeer o calculo da média
maiores_ou_iguais_25 = 0 # esta variável irá verificar se a idade é maior ou igual a 25 anos
menores_que_25 = 0 # esta variável irá verificar se a variável é menor a 25 anos

#criando o loop para executar de o que a questão sugere
while True:
    idade = int(input("\n Digite uma idade (-1 para sair): ")) # definindo o input para o usuário digitar a idade
    if idade == -1: # critério de parada para o laço (loop)
        break # critério para parar o laço (loop)
    #a variável total_idades será atribuida mais uma assim que o usuário informar mais uma nota:
    total_idades += 1
    ##a variável soma_idades será atribuida mais uma assim que o usuário informar mais uma nota:
    soma_idades += idade
    
    if idade >= 25: # se a idade for maior ou igual a 25, vai incrementar mais um
        maiores_ou_iguais_25 += 1
    else: # se não for maior ou igual a 25, obrigatoriamente será menor que 25, e também será uncrementado mais um
        menores_que_25 += 1

if total_idades > 0:
    media_idades = soma_idades / total_idades # foi declarada uma variável media_idades, para calcular a soma dividido pela quantidade
else:
    media_idades = 0 # caso contrário, a média das idades será 0

#imprimindo o que a questão solicitou

print(f"\n Total de idades válidas digitadas: {total_idades}")
print(f"\n Média das idades: {media_idades:.2f}")
print(f"\n Quantidade de idades >= 25: {maiores_ou_iguais_25}")
print(f"\n Quantidade de idades < 25: {menores_que_25}")




