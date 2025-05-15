'''5. Faça um programa que leia um número de celular, e corrija o número no caso deste
conter somente 8 dígitos, adicionando o '9' na frente. O usuário pode informar o número
com ou sem o traço separador.'''

'''
len(str(numero)) foi usada para obter o número de dígitos
int(input('')) foi usada para solicitar uma entrada e converter para um número inteiro. 
    
'''

print('Digite o número de celular')
number = int(input('Celular: '))
new_number = ''
if len(str(number)) < 9: 
    diferenca = 9 - len(str(number))
    new_number = '9' * diferenca

formatted = new_number + str(number)
formatted = formatted[0:5] + '-' + formatted[5:]

print('O celular possui %d dígitos. Acrescentando o digito "9" na frente.' % len(str(number)))
print('Exibindo corrigido sem formatação: %d' % number)
print('O celular corrigido com formatação é: %s' %formatted)