# questão  feita por João Henriue Ayres Pereira

'''2) Uma loja online deseja criar um sistema de avaliação de produtos. O usuário deve
inserir uma nota de 1 a 5 para um produto. Se uma nota inválida for digitada o usuário
deverá ser alertado. O programa deve calcular a média das notas. Continue coletando
notas até que o usuário insira -1.'''

#criando uma função sistema avaliação para executar o código
def sistema_avalicao_produto():
    #criando 2 variáveis contadoras para executar dentro do loop while
    soma_notas = 0 # esta variável irá fazer a soma das notas para posteriormente fazeer o calculo da média
    total_notas = 0 # esta variável irá receber a quantidade total de notas que o usuário informar
    while True:
        #criando o input para o usuário poder informar a nota:
        nota_avaliacao = int(input("\n Gostaríamos de receber sua avaliação sobe o produto (1 a 5): "))
        #critério de interrupção do laço (loop) conforme a questão sugere
        if nota_avaliacao == -1:
            break # foi usado um break como condição de parada do lop, caso não, continuaria rodando infinitamente
        #a variável total_notas será atribuida mais uma assim que o usuário informar mais uma nota:
        total_notas +=1
        #a variável soma_notas será a quentidade de notas que o usuário informar
        soma_notas += nota_avaliacao

        #se a variável nota_avaliacao for maior que 5 ou igual a 0, a nota informada será inválida
        if nota_avaliacao > 5 or nota_avaliacao == 0:
            print("\n Nota inválida")
    #se a variável total_notas ffor maior que 0, significa que temos como calcular média, que por ssua vez, se dá pela soma dividido pela quantidade
    if total_notas > 0:
        media_notas= soma_notas/total_notas
        #caso contrário a média será igual a 0
    else:
        media_notas = 0
    #imprimindo no console a média das notas:
    print(f"\n Média das notas: {media_notas:.2f}")

#chamando a função para poder executar o código:
sistema_avalicao_produto()
