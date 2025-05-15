def validar_email_simples(email):
  """
  Verifica se uma string (e-mail) contém o caractere '@'.

  Args:
    email: A string que representa o e-mail a ser validado.

  Returns:
    True se o e-mail contiver '@', False caso contrário.
  """
  if '@' in email:
    return True
  else:
    return False



while True:  # Cria um loop infinito
    
    email_digitado = input("Digite o e-mail a ser verificado (ou digite 'sair' para terminar): ")

    
    if email_digitado.lower() == 'sair':
        print("Programa encerrado.")
        break  

    
    eh_valido = validar_email_simples(email_digitado)


    if eh_valido:
        print("e-mail válido")
    else:
        print("e-mail inválido")

    print("-" * 20)