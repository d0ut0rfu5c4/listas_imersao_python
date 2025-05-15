# 3) faça um programa que leia um número e exiba o dia correspondente da semana
# 1 - domingo 2 - segunda, 3 - terça etc... Exiba "Valor inválido" caso um número
# inesperado for informado

day_of_week = input("\n informe o dia da semana, sendo 1 - domingo, 2 - Segunda-feira, 3 - Terça-feira, 4 - Quarta-feira, 5 - Quinta-feira, 6 - Sexta-feira, 7 - Sábado : ")
print()

match day_of_week:
    case '1':
        print("\n Domingo")
    case '2':
        print("\n Segunda-feira")
    case '3':
        print("\n Terça-feira")
    case '4':
        print("\n Quarta-feira")
    case '5':
        print("\n Quinta-feira")
    case '6':
        print("\n Sexta-feira")
    case '7':
        print("\n Sábado")
    case _:
        print("\n Valor não compatível, tente novamente")