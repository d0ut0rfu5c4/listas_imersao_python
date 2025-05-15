# Função para calcular a média dos tempos
def calcular_media(tempos):
    return sum(tempos) / len(tempos)

# Função para encontrar o campeão
def encontrar_campeao(tempos_corredores):
    menor_media = float('inf')
    campeao = ""

    for nome, tempos in tempos_corredores.items():
        media = calcular_media(tempos)
        if media < menor_media:
            menor_media = media
            campeao = nome

    return campeao, round(menor_media, 2)

# Programa principal
tempos_corredores = {}

for i in range(4):
    nome = input(f"Digite o nome do {i+1}º corredor: ")
    tempos = []
    for j in range(3):
        tempo = float(input(f"Digite o tempo da {j+1}ª volta de {nome} (em segundos): "))
        tempos.append(tempo)
    tempos_corredores[nome] = tempos

campeao, media = encontrar_campeao(tempos_corredores)

print(f"\nCAMPEÃO: {campeao.upper()}")
print(f"MÉDIA DE TEMPO: {media:.2f} segundos")
