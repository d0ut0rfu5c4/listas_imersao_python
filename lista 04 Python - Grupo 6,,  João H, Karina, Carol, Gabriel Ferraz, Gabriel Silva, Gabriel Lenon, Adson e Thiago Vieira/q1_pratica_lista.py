'''
lista =  [] # criando ba lista vazia 

for i in range(10):
    numeros = int(input("\n\t informe valores inteiros: \t")) # fazendo o input
    lista.append(numeros) # adicionando os números na lista

soma = sum(lista)

print("\n\t A Soma equivale a: ", soma)

'''

# exercício02 - slide

'''
lista_numerica = []

for i in range(3):
    numeros = int(input("\n\t Digite 10 números: \t"))
    lista_numerica.append(numeros)

    menor_valor = min(lista_numerica)
    maior_valor = lista_numerica[i]
    indice_maior_valor = len(lista_numerica)

for _ in lista_numerica(3):
    qtd_impares = 0
    if qtd_impares % 2 == 0:
        print("\n\t Par")
    else:
        print("\n\t Ímpar")

print("\n\t A lista contém so seguintes valores: ", lista_numerica)
print("\n\t O Menor elemento da lista é: ", menor_valor)
print(f"\n\t O Maior elemento foi: {maior_valor} e seu indice da lista foi: {indice_maior_valor} ")
print(f"\n\t A quantidade de valores ímpares na lista é: {qtd_impares[i]}")
'''

lista_restaurante = []
lista_nota_avaliacao = []

# Loop para adicionar restaurantes
while True:
    nome_restaurante = input("\n\tInsira o nome do restaurante (ou 'PARE' para encerrar): ").strip()
    if nome_restaurante.upper() == 'PARE':
        break

    # Verifica se o restaurante já foi cadastrado
    if nome_restaurante in lista_restaurante:
        print("\n\tEste estabelecimento já foi incluído anteriormente!\n")
    else:
        lista_restaurante.append(nome_restaurante)
        notas = []

        # Loop para avaliações do mesmo restaurante
        while True:
            try:
                nota = float(input("\n\tInforme uma nota para este restaurante (0 a 5): "))
                if 0 <= nota <= 5:
                    notas.append(nota)
                    print("\n\tRestaurante avaliado com sucesso!\n")
                else:
                    print("\n\tNota inválida. Digite um valor entre 0 e 5.\n")
                    continue
            except ValueError:
                print("\n\tPor favor, insira um número válido.\n")
                continue

            # Pergunta se o usuário quer avaliar novamente o mesmo restaurante
            resposta = input("\n\tDeseja reavaliar este mesmo estabelecimento? (S/N): ").strip().upper()
            if resposta != 'S':
                break  # sai do loop de avaliação e volta para o de cadastro

        lista_nota_avaliacao.append(notas)
        print(f"\n\tAs avaliações para {nome_restaurante} foram salvas com sucesso!")

# Exibindo resumo
print("\n----- RESUMO DAS AVALIAÇÕES -----\n")
for i in range(len(lista_restaurante)):
    nome = lista_restaurante[i]
    notas = lista_nota_avaliacao[i]
    media = sum(notas) / len(notas)
    print(f"{nome}: média {media:.2f} baseada em {len(notas)} avaliação(ões)")
