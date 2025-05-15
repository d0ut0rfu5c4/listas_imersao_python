def menu():
    print("\nControle de Estoque")
    print("1. Incluir produto")
    print("2. Excluir produto")
    print("3. Atualizar estoque")
    print("4. Exibir todo o estoque")
    print("5. Calcular valor total do estoque")
    print("6. Sair")
    return input("Escolha uma opção: ")

def incluir_produto(estoque):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço unitário: "))
    estoque[nome] = [quantidade, preco]
    print(f'Produto "{nome}" adicionado ao estoque.')

def excluir_produto(estoque):
    nome = input("Digite o nome do produto a ser excluído: ")
    if nome in estoque:
        del estoque[nome]
        print(f'Produto "{nome}" removido do estoque.')
    else:
        print("Produto não encontrado no estoque.")

def atualizar_estoque(estoque):
    nome = input("Digite o nome do produto a ser atualizado: ")
    if nome in estoque:
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        estoque[nome][0] = nova_quantidade
        print(f'Estoque de "{nome}" atualizado para {nova_quantidade} unidades.')
    else:
        print("Produto não encontrado no estoque.")

def exibir_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return
    print("\nLista de Produtos em Estoque:")
    for nome, (quantidade, preco) in estoque.items():
        print(f'Nome: {nome}\nQuantidade em Estoque: {quantidade} unidades\nPreço Unitário: R$ {preco:.2f}\n')

def calcular_valor_total(estoque):
    valor_total = sum(quantidade * preco for quantidade, preco in estoque.values())
    print(f'Valor total do estoque: R$ {valor_total:.2f}')

def main():
    estoque = {}
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            incluir_produto(estoque)
        elif opcao == '2':
            excluir_produto(estoque)
        elif opcao == '3':
            atualizar_estoque(estoque)
        elif opcao == '4':
            exibir_estoque(estoque)
        elif opcao == '5':
            calcular_valor_total(estoque)
        elif opcao == '6':
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


    main()