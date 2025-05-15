#Questão feita por Gabriel Ferraz Millet

# -*- coding: utf-8 -*-

# Inicializa um conjunto (set) para armazenar nomes de produtos únicos
tipos_produtos = set() # Renomeado para clareza em português

print("--- Sistema de Controle de Estoque ---")
print("Digite 'FIM' no nome do produto para encerrar.")

while True:
    # Solicita o nome do produto
    # .strip() remove espaços em branco antes e depois do nome
    nome_produto_input = input("\nDigite o nome do produto: ").strip()

    # Verifica a condição de encerramento (ignora maiúsculas/minúsculas)
    if nome_produto_input.upper() == "FIM":
        break # Sai do loop principal

    # Validação básica: Garante que o nome não seja vazio após remover espaços
    if not nome_produto_input:
         print("Erro: O nome do produto não pode estar vazio. Tente novamente.")
         continue # Volta ao início do loop principal para pedir o nome

    # Guarda o nome válido para usar adiante
    nome_produto = nome_produto_input

    # Loop para obter uma quantidade válida para o produto atual
    while True:
        try:
            # Solicita a quantidade
            quantidade_texto = input(f"Digite a quantidade para '{nome_produto}': ")
            quantidade = int(quantidade_texto) # Tenta converter para número inteiro

            # Valida a quantidade (não pode ser negativa)
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa. Tente novamente.")
                # Continua no loop interno (pede a quantidade novamente)
            else:
                # Quantidade válida foi inserida
                # Adiciona o nome do produto ao conjunto (duplicados são ignorados automaticamente)
                tipos_produtos.add(nome_produto) # Armazena o nome já validado e sem espaços extras
                print(f"-> Registrado: Produto '{nome_produto}' com quantidade {quantidade}.")
                break # Sai do loop interno (de quantidade) e volta a pedir novo produto

        except ValueError:
            # Ocorre se a entrada não puder ser convertida para inteiro
            print("Erro: Quantidade inválida. Por favor, insira um número inteiro.")
            # Continua no loop interno (pede a quantidade novamente)
        except Exception as e:
             # Captura outros erros inesperados durante a leitura da quantidade
             print(f"Erro inesperado ao ler a quantidade: {e}")
             # Continua no loop interno

# Após o término do loop (usuário digitou "FIM")
print("\n--- Encerramento do Sistema ---")
# Exibe a contagem de itens no conjunto, que representa os tipos únicos
print(f"Total de tipos de produtos diferentes inseridos: {len(tipos_produtos)}")

# Bloco Opcional: Exibe os tipos únicos de produtos inseridos (para verificação)
# Descomente as linhas abaixo se quiser ver a lista
#
# print("-" * 35) # Linha separadora
# if tipos_produtos:
#     print("Tipos de produtos registrados (em ordem alfabética):")
#     # Converte o conjunto para lista, ordena e itera para exibir
#     for produto in sorted(list(tipos_produtos)): # Ordena para melhor legibilidade
#         print(f"- {produto}")
# else:
#     print("Nenhum tipo de produto foi inserido.")
# print("-" * 35) # Linha separadora