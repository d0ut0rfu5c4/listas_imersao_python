# feita por Carol Sousa

#questão 2 lista 4
# Inicializar uma lista para armazenar as médias
medias = []

# Solicitar as notas dos estudantes
for i in range(5):  # Loop para 5 estudantes
    print(f"Estudante {i + 1}:")
    nota1 = float(input("Digite a primeira nota: "))  # Primeira nota
    nota2 = float(input("Digite a segunda nota: "))   # Segunda nota
    
    # Calcular a média
    media = (nota1 + nota2) / 2  # Cálculo da média das duas notas
    medias.append(media)          # Adicionar a média à lista de médias

# Imprimir a lista de médias
print("\nLista de Médias dos Estudantes:")
print(medias)

# Contar quantos estudantes têm média >= 7.0
estudantes_aptos = sum(1 for media in medias if media >= 7.0)

# Imprimir o número de estudantes com média >= 7.0
print(f"Número de estudantes com média >= 7.0: {estudantes_aptos}")