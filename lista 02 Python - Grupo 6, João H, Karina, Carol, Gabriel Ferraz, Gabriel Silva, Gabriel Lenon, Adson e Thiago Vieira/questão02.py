# 2) Escreva um algorítimo que receba o código correspondente ao cargo de um funcionário
# de uam escola e seu salário atual. Mostre o valor do novo salário.

def Cargo_funcionario():
    corresponding_code = (input("selecione de 1 a 5, o código correspondente ao seu cargo: "))
    salary = float(input("Informe seu salário atual: (em R$): "))
    new_salary = 0
    match corresponding_code:
        case '1':
            new_salary = salary + (salary * 0.45) 
        case '2':
            new_salary = salary + (salary * 0.35)
        case '3':
            new_salary = salary + (salary * 0.25)
        case '4':
            new_salary = salary + (salary * 0.15)
        case '5':
            print("\n Não há aumento salarial ")
        case _ :
            print("Número inválido! Tente outra vez..")

    print(corresponding_code, "\n Para este cagrgo, o salario atualizado : R$", new_salary)

Cargo_funcionario()