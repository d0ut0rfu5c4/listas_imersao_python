def substituir_palavra_e_maiusculas():
  """
  Pede ao usuário uma frase, uma palavra a ser substituída e a nova palavra.
  Substitui a palavra e exibe a frase modificada em letras maiúsculas.
  """
  frase = input("Digite uma frase: ")
  palavra_antiga = input("Digite a palavra que você quer substituir: ")
  palavra_nova = input("Digite a palavra que você quer colocar no lugar: ")

  frase_modificada = frase.replace(palavra_antiga, palavra_nova).upper()
  print(frase_modificada)

# Chama a função para executar o programa
substituir_palavra_e_maiusculas()