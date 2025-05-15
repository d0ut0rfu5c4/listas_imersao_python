# 6) Uma rede de cinemas deseja criar um sistema para controlar a venda de ingressos. Eles
# possuem três tipos de sessões: Matinê, Vespertina e Noturna. Cada sessão tem um preço
# diferente. As regras são:
# 1. Sessão Matinê: Custa R$ 20.
# 2. Sessão Vespertina: Custa R$ 25.
# 3. Sessão Noturna: Custa R$ 30.
# Crianças até 12 anos, estudantes e idosos (65+) têm direito a 50% de desconto em
# qualquer sessão. Escreva um programa que peça ao usuário para escolher o tipo de
# sessão e informar a idade. Caso o usuário não seja idoso ou criança, ele deverá informar
# se é estudante. O programa deve informar o valor total da compra.

def cinema_session():
    print("\n Escolha uma sessão:  1 -> Sessão Matinê   2 -> Sessão Vespertina   3 -> Sessão Noturna \n\n")
    sessao = input("\n Qual a sessão de cinema que gostaria de entrar: ")
    idade = int(input("\n Qual sua idade ? "))
    estudante = input("\n Você é estudante ? ")
    match sessao:
        case '1':
            valor_sessao = 20
        case '2':
            valor_sessao = 25
        case '3':
            valor_sessao = 30
        case _:
            print("\n Valor não correspondente! \n")

    valor_desconto = valor_sessao/2
    if idade >= 65 or idade <= 12 or estudante == 'S' or estudante == 's':
        print("\n Você tem direito a  50 por cento de desconto! \n")
    else:
        print("\n Você não tem direito a desconto \n")

    print("\n Valor do ingresso: R$ ", valor_desconto)

cinema_session()

    
    