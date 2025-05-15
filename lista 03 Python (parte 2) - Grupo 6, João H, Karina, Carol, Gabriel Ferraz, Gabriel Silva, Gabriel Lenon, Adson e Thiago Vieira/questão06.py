# feito por Karina Meirles Varela

maior_numero_par = None

for x in range(10):
    num = int(input("Digite um número: "))
    
    
    if num % 2 == 0:
        if maior_numero_par is None or num > maior_numero_par:
            maior_numero_par = num
            
if maior_numero_par is not None:
    print(f"Maior número par: {maior_numero_par}")
else:
    print("Nenhum número par foi digitado.")