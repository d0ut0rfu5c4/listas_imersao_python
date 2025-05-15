def buscar_contato(agenda, nome):
    if nome in agenda:
        print(f"Número de telefone de {nome}: {agenda[nome]}.")
    else:
        print("Contato não encontrado na agenda.")

def main():
    agenda = {}
    while True:
        print("\nMenu:")
        print("1. Incluir contato")
        print("2. Excluir contato")
        print("3. Buscar contato")
        print("4. Finalizar programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o número de telefone: ")
            incluir_contato(agenda, nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome do contato a ser excluído: ")
            excluir_contato(agenda, nome)
        elif opcao == "3":
            nome = input("Digite o nome do contato a ser buscado: ")
            buscar_contato(agenda, nome)
        elif opcao == "4":
            print("\nAgenda:")
            print(agenda)
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()