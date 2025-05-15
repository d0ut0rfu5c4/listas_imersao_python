def quadrado(x):
  dicionario_quadrados = {}
  if not isinstance(x, int) or x < 1:
    return dicionario_quadrados
  for numero in range(1, x + 1):
    valor_quadrado = numero * numero
    dicionario_quadrados[numero] = valor_quadrado
  return dicionario_quadrados

if _name_ == "_main_":
  print("--- Calculadora de Quadrados em Dicionário ---")
  print("Digite um número inteiro para calcular os quadrados.")
  print("Digite 'sair' ou 'fim' para encerrar o programa.")

  while True:
    try:
      entrada_str = input("\nDigite um número inteiro para 'x' (ou 'sair'/'fim'): ").strip().lower()

      if entrada_str == "sair" or entrada_str == "fim":
        print("Encerrando o programa...")
        break

      numero_x = int(entrada_str)

      resultado = quadrado(numero_x)

      if resultado:
        print("Saída:")
        print(resultado)
      else:
        print(f"Erro: O número deve ser um inteiro maior ou igual a 1. Você digitou: {numero_x}")

    except ValueError:
      print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'sair'/'fim'.")
    except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")

  print("\n--- Fim do Programa ---")