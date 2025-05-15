# feito por Thiago Vieira

# 4) Faça um programa que:
# - Receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# - Calcule a média anual de temperaturas
# - Exiba todos os meses que têm as temperaturas acima da média anual (mostrar o mês por extenso: Janeiro, Fevereiro, . . . ). 
# Dica: Crie uma lista de strings com todos os nomes dos meses.

months_of_the_year = ["Janeiro" , "Fevereiro" , "Março" , "Abril" , 
                      "Maio" , "Junho" , "Julho" , "Agosto" , 
                      "Setembro" , "Outubro" , "Novembro" , "Dezembro"]

month_temperature = []
temperature_sum = 0

for month in months_of_the_year:
    temp = float(input(f"Informe a temperatura do mês de {month} (°C): "))
    month_temperature.append(temp)

for temperature in month_temperature:
    temperature_sum += temperature

average_temp = temperature_sum / len(months_of_the_year)

print(f"\nTemperatura média: {average_temp}°C")
print("Meses com a temperatura acima da média: \n")

for i in range(len(month_temperature)):
    if month_temperature[i] > average_temp:
        print(months_of_the_year[i],": ", month_temperature[i],"°C")

print()