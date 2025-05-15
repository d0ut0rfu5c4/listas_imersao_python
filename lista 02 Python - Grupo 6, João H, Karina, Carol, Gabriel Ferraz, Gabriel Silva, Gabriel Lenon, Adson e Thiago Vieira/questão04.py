# 4) Em uma cidade, a prefeitura deseja classificar os motoristas com base em suas infrações de trânsito no
# último ano. O objetivo é criar um programa de reeducação para os motoristas que cometem infrações. para isso
# oeles deffiniram as seguintes categorias:

# a) Motorista Exemplar: não cometeu

while True:   

    drivers_ratings = None
    infracoes = int(input("\n Informe a quantidade de infrações que você teve no último ano:"))
    if infracoes == 0:
        drivers_ratings = "exemplar"
    elif 0 < infracoes <= 3:
        drivers_ratings = "atento"
    elif 3 < infracoes <= 6:
        drivers_ratings = "desatento"
    elif infracoes > 6:
        drivers_ratings = "perigoso"
    else:
        print("Valor Inválido")
    if drivers_ratings != None:
        print(f"\n Com base na quantidade de infrações informada ({infracoes}), você é um motorista {drivers_ratings}.\n")