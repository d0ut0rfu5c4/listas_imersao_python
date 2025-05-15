'''6) Faça um programa que leia o nome e três notas de 3 estudantes. Os nomes e as médias
devem ser armazenadas, cada um, em uma lista. Por fim, em outra estrutura de
repetição, exiba o nome e a média, um a um, formatando o nome para ser exibido com a
primeira letra maiúscula e o restante minúscula e a média para apenas duas casas
decimais. Informe também se o estudante está aprovado ou reprovado. Obs: Para ser
aprovado a média deve ser maior ou igual a 7.'
'''

# Listas para armazenar os nomes e médias
nomes = []
medias = []

# For para ler os dados de 3 estudantes
for i in range(3): #range para sequência de números
    nome = input(f"Digite o nome do {i+1}º estudante: ") #{i+} incrmento...
    notas = []
    
    for j in range(3):  # for para ler as 3 notas do estudante
        nota = float(input(f"Digite a {j+1}ª nota de {nome}: "))
        notas.append(nota)    
   
    media = sum(notas) / len(notas)  # Calcular a média das notas
    
    # Armazenar o nome e a média nas listas correspondentes
    nomes.append(nome) #adiciona um item ao final
    medias.append(media)

# Exibir os resultados
print("\nResultado final:")
for i in range(3):
    nome_formatado = nomes[i].capitalize() #Formatar com a primeira letra maiúscula e o restante minúscula
    media_formatada = f"{medias[i]:.2f}" # Formatar a média para duas casas decimais
    
    # Verificar se o estudante está aprovado ou reprovado
    status = "está aprovado" if medias[i] >= 7 else "está reprovado"
    
    # Exibir o nome, a média e o status
    print(f"A média de {nome_formatado} é {media_formatada} e ele(a) está {status}")

