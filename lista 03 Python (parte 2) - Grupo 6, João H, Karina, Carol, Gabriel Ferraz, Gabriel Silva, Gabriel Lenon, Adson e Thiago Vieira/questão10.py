# feito por Gabriel Silva

#Exercício 10:

print("\nEste programa irá calcular a sequência de fibonacci para dois números inteiros aleatórios que você inserir!\n\n")
num1 = int(input("Informe o valor do primeiro dígito:\n"))
num2 = int(input("Informe o valor do segundo dígito:\n"))
print(f"{num1}")
print(f"{num2}")

for i in range (20):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(f"{num3}")