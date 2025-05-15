# feita por João Henrique Ayres Pereira

'''5) Uma loja deseja avaliar o desempenho de seus vendedores. Crie um programa que:

○ Solicite ao usuário o número total de vendedores da loja.
○ Para cada vendedor, peça ao usuário o nome do vendedor e o total de vendas
realizadas no ano.
○ Determine o vendedor com o maior volume de vendas e o vendedor com o
menor volume.
○ Exiba o nome de todos os vendedores e suas vendas totais, destacando o
vendedor com as vendas mais altas e o vendedor com as vendas mais baixas.'''

def avaliar_vendedores():
    vendedores = []
    
    num_vendedores = int(input("\n\n Digite o número total de vendedores: \t"))
    
    for _ in range(num_vendedores):
        nome = input("\n\n Digite o nome do vendedor: \t")
        vendas = float(input(f"\n Digite o total de vendas de {nome} no ano: \t"))
        vendedores.append((nome, vendas))
    
    vendedor_mais_vendas = max(vendedores, key=lambda x: x[1])
    vendedor_menos_vendas = min(vendedores, key=lambda x: x[1])
    
    print("\nDesempenho dos vendedores:\n\n")
    for nome, vendas in vendedores:
        destaque = "- Maior volume de vendas!" if nome == vendedor_mais_vendas[0] else "- menor volume de vendas" if nome == vendedor_menos_vendas[0] else ""
        print(f"{nome}: R$ {vendas:.2f} {destaque}")

if __name__ == "__main__":
    avaliar_vendedores()
