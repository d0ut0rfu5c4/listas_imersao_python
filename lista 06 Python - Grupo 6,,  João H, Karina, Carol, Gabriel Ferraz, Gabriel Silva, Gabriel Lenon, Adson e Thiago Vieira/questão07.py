'''Q7 - Crie um programa que represente uma agenda de contatos. O programa deve
oferecer as seguintes opções ao usuário:
1. Incluir contato: Permite ao usuário adicionar um nome e um número de
telefone à agenda.
2. Excluir contato: Permite ao usuário remover um contato da agenda
usando o nome como referência.
3. Buscar contato: Permite ao usuário buscar um contato na agenda pelo
nome e exibir o número de telefone correspondente.
4. Sair. Exibe todo o dicionário e a mensagem “Programa finalizado.”.
Use um dicionário onde as chaves são os nomes dos contatos e os valores são os
números de telefone.'''

def menu():
    print("\nagenda de contatos")
    print("1. Incluir o contato")
    print("2. Excluir o contato")
    print("3. Buscar o contato")
    print("4. Sair")
    return input("Escolha uma das opção por favor ")

def main():
    agenda = {}
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome = input("digite nome contato: ")
            telefone = input("digite número de telefone: ")
            agenda[nome] = telefone
            print("Contato foi adicionado com sucesso!")
        
        elif opcao == '2':
            nome = input("digite nome do contato a ser excluído: ")
            if nome in agenda:
                del agenda[nome]
                print("Contato excluído com sucesso")
            else:
                print("Contato não encontrado na agenda.")
        
        elif opcao == '3':
            nome = input("Digite o nome do contato a ser encontrado: ")
            if nome in agenda:
                print(f"Número de telefone de {nome}: {agenda[nome]}")
            else:
                print("Contato não encontrado na agenda.")
        
        elif opcao == '4':
            print("\nAgenda:")
            print(agenda)
            print("Programa será finalizado.")
            break
        
        else:
            print("Opção inválida. Tente mais uma novamente.")

if _name_ == "_main_":
    main()