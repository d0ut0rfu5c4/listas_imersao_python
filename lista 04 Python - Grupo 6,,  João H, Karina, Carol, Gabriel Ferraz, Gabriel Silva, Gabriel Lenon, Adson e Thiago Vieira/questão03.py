# feito por Thiago Vieira

# 3) Faça um programa em duas partes:
# - Parte 01: Ler 10 números inteiros e armazená-los em uma lista única.
# - Parte 02: Em uma nova estrutura de repetição, armazene os números pares na lista PARES e os números ímpares na lista ÍMPARES.
# - Imprima as três listas.

numbers_list = []
even_numbers_list = []
odd_numbers_list = []
user_number = None

#Parte 1
for i in range(10):
    user_number = int(input("Insira o número: "))
    numbers_list.append(user_number)

#Parte 2
for number in numbers_list:
    if number % 2 == 0:
        even_numbers_list.append(number)
    else:
        odd_numbers_list.append(number)


print("\n",numbers_list)
print("\n",even_numbers_list)
print("\n",odd_numbers_list)

