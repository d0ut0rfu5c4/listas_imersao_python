# feito por João Henrique Ayres Pereira

'''
6) Desenvolva um programa que permita aos usuários avaliarem restaurantes com notas de
0 a 5. Cada restaurante só deve ser inserido uma vez na lista. Se um restaurante for
avaliado mais de uma vez, o programa deve atualizar a nota média do restaurante
considerando todas as avaliações fornecidas até o momento, mas o restaurante não deve
ser adicionado novamente à lista.
O programa deve:
● Solicitar o nome do restaurante ou digitar “PARE” para finalizar.
● Solicitar a nota dada pelo usuário (de 0 a 5).
● Se o restaurante já foi avaliado anteriormente, atualizar a nota média
considerando todas as avaliações anteriores e a nova avaliação. Use a seguinte
fórmula: nova média =

média anterior × número de avaliações + nova nota
número de avaliações + 1

Ao final, o programa deve mostrar o restaurante com a maior nota média e o restaurante
com a menor nota média.

'''

# variáveis utilizadas e suas funções:
# 1) nome_restaurante -> vai solicitar o nome do restaurante para o usuário digitar
# 2) lista_restaurante -> é a lista de restaurante que vai receber o input de nome_restaurante
# 3) lista_nota_avaliacao -> é a lista das notas de avaliação que vai receber o input das notas
# 4) notas -> vai soliciitar as notas de avaliação para o usuário inserirr
# 5) media -> fará o cálculo da média das notas dividido pela quantidade de notas
# 6) maior_media -> calcula a maior média
# 7) menor-media -> calcula a menor média


# Dica: use listas para armazenar os nomes dos restaurarntes, suas notas médias e a contagem de 
# avaliações para cada restaurante, lembr-se que cada restaurante deve aparecer na lista apenas 1 vez

lista_restaurante = []
lista_nota_avaliacao = []

# Loop para adicionar restaurantes
while True:
    nome_restaurante = input("\n\t Insira o nome do restaurante (ou 'PARE' para encerrar): ").strip()
    if nome_restaurante.upper() == 'PARE':
        break

    # Verifica se o restaurante já foi cadastrado na lista
    if nome_restaurante in lista_restaurante:
        print("\n\tEste estabelecimento já foi incluído anteriormente!\n")
    else:
        lista_restaurante.append(nome_restaurante)
        notas = []

        # Loop para avaliações do mesmo restaurante
        while True:
            try:
                nota = float(input("\n\t Informe uma nota para este restaurante (0 a 5): \t"))
                if 0 <= nota <= 5:
                    notas.append(nota)
                    print("\n\t Restaurante avaliado com sucesso!\n")
                else:
                    print("\n\tNota inválida. Digite um valor entre 0 e 5.\n")
                    continue
            except ValueError:
                print("\n\t Por Gentileza, insira um número válido.\n")
                continue

            # Pergunta se o usuário quer avaliar novamente o mesmo restaurante
            resposta = input("\n\tDeseja reavaliar este mesmo estabelecimento? (S -> Sim/N -> Não): ").strip().upper()
            if resposta != 'S':
                break

        lista_nota_avaliacao.append(notas)
        print(f"\n\tAs avaliações para {nome_restaurante} foram salvas com sucesso!")

# Exibindo resumo
print("\n\t----- RESUMO DAS AVALIAÇÕES DOS RESTAURANTES -----\n\n")

medias = []
for i in range(len(lista_restaurante)):
    nome = lista_restaurante[i]
    notas = lista_nota_avaliacao[i]
    media = sum(notas) / len(notas)
    medias.append(media)
    print(f"{nome}: média {media:.1f} baseada em {len(notas)} avaliação(ões)")

# Encontrando maior e menor média utilizando funções
maior_media = max(medias)
menor_media = min(medias)
indice_maior = medias.index(maior_media)
indice_menor = medias.index(menor_media)

print("\n\t----- RANKING MELHORES E PIORES AVALIAÇÕES -----\n\n")
print(f"\n\t Restaurante com a MELHOR média: {lista_restaurante[indice_maior]} ({maior_media:.1f})")
print(f"\n\t Restaurante com a PIOR média: {lista_restaurante[indice_menor]} ({menor_media:.1f})")





   
