# feita por Carol Sousa

# questão 1
# Criando as variáveis
idades = []
idade = 0

# Leitura das idades
while True:
    idade = int(input("Digite uma idade (ou -1 para encerrar): "))
    
    if idade == -1:
        break  # Encerra a entrada de dados
    idades.append(idade)  # Armazena a idade

# Verificações após a entrada de dados
quantidade_idades = len(idades)

if quantidade_idades > 0:
    # Exibir a quantidade de idades válidas
    print(f"\nQuantidade de idades válidas: {quantidade_idades}")
    
    # Exibir as idades armazenadas
    print(f"Idades armazenadas: {idades}")
    
    # Calcular e mostrar a média das idades
    media_idades = sum(idades) / quantidade_idades
    print(f"Média das idades: {media_idades:.2f}")
    
    # Calcular e mostrar a quantidade de idades acima da média
    idades_acima_media = [idade for idade in idades if idade > media_idades]
    quantidade_acima_media = len(idades_acima_media)
    print(f"Quantidade de idades acima da média: {quantidade_acima_media}")
    
    # Exibir a maior e menor idade
    maior_idade = max(idades)
    menor_idade = min(idades)
    print(f"Maior idade: {maior_idade}")
    print(f"Menor idade: {menor_idade}")
    
    # Calcular e mostrar a quantidade de valores abaixo de 18
    quantidade_baixo_18 = len([idade for idade in idades if idade < 18])
    print(f"Quantidade de valores abaixo de 18: {quantidade_baixo_18}")

else:
    print("Nenhuma idade válida foi informada.")