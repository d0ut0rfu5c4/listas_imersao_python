# Questão feita por Gabriel Ferraz Millet

# -*- coding: utf-8 -*-
"""
Sistema simples para registrar serviços de um petshop para 10 cachorros
e exibir a contagem final de cada serviço.
"""

def controle_petshop():
    """
    Registra os serviços realizados em 10 cachorros e exibe a contagem final
    para cada tipo de serviço.
    """
    # Dicionário para armazenar a contagem de cada serviço
    # As chaves são os códigos dos serviços, e os valores são as contagens
    contagem_servicos = {
        1: 0,  # Banho
        2: 0,  # Tosa
        3: 0,  # Banho e Tosa
        4: 0   # Outros
    }

    # Dicionário para mapear códigos para nomes (para melhor feedback ao usuário)
    nomes_servicos = {
        1: "Banho",
        2: "Tosa",
        3: "Banho e Tosa",
        4: "Outros"
    }

    num_cachorros = 10 # Número fixo de cachorros atendidos

    print("--- Controle de Serviços do Petshop ---")
    print(f"Por favor, insira o código do serviço para cada um dos {num_cachorros} cachorros.")

    # Loop para processar cada cachorro
    for i in range(num_cachorros):
        print("-" * 30) # Linha separadora
        print(f"Cachorro {i + 1} de {num_cachorros}:")

        # Loop para garantir que a entrada seja válida (1, 2, 3 ou 4)
        while True:
            # Exibe as opções de serviço claramente
            print("\nOpções de Serviço Disponíveis:")
            for codigo, nome in nomes_servicos.items():
                print(f"  {codigo} - {nome}")

            try:
                # Solicita o código do serviço ao usuário
                codigo_input = input("Digite o código do serviço desejado: ").strip() # .strip() remove espaços extras

                # Tenta converter a entrada para um número inteiro
                codigo_servico = int(codigo_input)

                # Verifica se o código é uma das chaves válidas no dicionário
                if codigo_servico in contagem_servicos:
                    # Incrementa o contador para o serviço correspondente
                    contagem_servicos[codigo_servico] += 1
                    # Exibe confirmação do registro
                    print(f"-> OK! Serviço '{nomes_servicos[codigo_servico]}' registrado para o cachorro {i + 1}.")
                    break # Sai do loop de validação (while True) e vai para o próximo cachorro (próxima iteração do for)
                else:
                    # Informa que o código numérico não é uma opção válida
                    print("\n*** Erro: Código de serviço inválido. ***")
                    print("*** Por favor, digite apenas 1, 2, 3 ou 4. ***")

            except ValueError:
                # Ocorre se o usuário digitar algo que não pode ser convertido para int (ex: letras, vazio)
                print("\n*** Erro: Entrada inválida. ***")
                print("*** Por favor, digite um NÚMERO correspondente ao código do serviço. ***")
            except Exception as e:
                # Captura outros erros inesperados (raro neste caso, mas boa prática)
                print(f"\n*** Ocorreu um erro inesperado: {e} ***")
                # Pode ser útil adicionar um 'continue' aqui ou decidir parar o programa

    # --- Fim do loop dos cachorros ---

    # Após processar todos os cachorros, exibe o resumo final
    print("\n" + "=" * 40) # Linha separadora mais longa
    print("     Resumo dos Serviços Realizados")
    print("=" * 40)

    # Itera sobre o dicionário de nomes para exibir os resultados de forma organizada
    for codigo, nome in nomes_servicos.items():
        quantidade = contagem_servicos[codigo] # Pega a contagem final para este serviço
        # Formata a saída para alinhar os resultados
        print(f"{nome:<15}: {quantidade} solicitações") # Alinha o nome à esquerda em 15 espaços

    print("=" * 40)
    print("--- Fim do Programa ---")

# --- Fim da definição da função ---

# Bloco principal: Executa a função controle_petshop() quando o script é rodado
if __name__ == "__main__":
    controle_petshop()