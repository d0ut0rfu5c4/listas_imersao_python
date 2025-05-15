# 8) Converta uma temperatura em graus Celsius C para Fahrenheit F.
#Utilize a fórmula: F = 9/5C + 32

print()

def Converter_temperatura():
    temp_celsius = float(input("Digite a temperatura a ser convertida: "))
    temp_fahreheint = 9/5 * temp_celsius + 32
    print(temp_celsius, "°C em Fahreheint é: ", temp_fahreheint)

Converter_temperatura()
