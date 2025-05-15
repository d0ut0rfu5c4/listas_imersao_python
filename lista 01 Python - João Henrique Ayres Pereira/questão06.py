# 6) Dado um raio r, calcule e mostre a área de um círculo

def area_circulo():
    PI = 3.14159265359
    raio = float(input("defina o raio da circunferência: "))
    area = PI * (raio ** 2)
    print("A Área do círculo equivale a:", area)

area_circulo()