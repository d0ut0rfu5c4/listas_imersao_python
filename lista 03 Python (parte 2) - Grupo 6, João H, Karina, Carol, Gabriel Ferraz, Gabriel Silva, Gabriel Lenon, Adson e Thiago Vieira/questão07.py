# fita por Carol Sousa

# questao 7
# Solicitar a quantidade de clientes
num_clientes = int(input("Quantos clientes há na academia? "))

# Inicializar variáveis
clientes = []
maior_altura = 0
menor_altura = float('inf')
maior_peso = 0
menor_peso = float('inf')
soma_alturas = 0
soma_pesos = 0

for _ in range(num_clientes):
    codigo = input("Digite o código do cliente: ")
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))
    
    # Adicionar cliente à lista
    clientes.append((codigo, altura, peso))
    
    # Calcular maior e menor altura
    if altura > maior_altura:
        maior_altura = altura
        codigo_maior = codigo
        peso_maior = peso  # Armazena o peso do cliente mais alto
    if altura < menor_altura:
        menor_altura = altura
        codigo_menor = codigo
        peso_menor = peso  # Armazena o peso do cliente mais baixo

    # Calcular maior e menor peso
    if peso > maior_peso:
        maior_peso = peso
        codigo_maior_peso = codigo
        altura_maior_peso = altura  # Armazena a altura do cliente mais pesado
    if peso < menor_peso:
        menor_peso = peso
        codigo_menor_peso = codigo
        altura_menor_peso = altura  # Armazena a altura do cliente mais leve

    # Acumular para médias
    soma_alturas += altura
    soma_pesos += peso

# Calcular médias
media_alturas = soma_alturas / num_clientes
media_pesos = soma_pesos / num_clientes

# Exibir resultados
print(f"Cliente mais alto: {codigo_maior}, Altura: {maior_altura}, Peso: {peso_maior}")
print(f"Cliente mais baixo: {codigo_menor}, Altura: {menor_altura}, Peso: {peso_menor}")
print(f"Cliente mais pesado: {codigo_maior_peso}, Altura: {altura_maior_peso}, Peso: {maior_peso}")
print(f"Cliente mais leve: {codigo_menor_peso}, Altura: {altura_menor_peso}, Peso: {menor_peso}")
print(f"Média das alturas: {media_alturas}")
print(f"Média dos pesos: {media_pesos}")