import math

print("3) Dadaos os aldos a,b e c de um triângulo, calcule sua área. Calcule sua área, use a formula de Heron: raíz quadrada de (s-a) (s-b) (s-c), onde o semiperímetrp=o s = a+b+c/2")

print()

a = float(input("Insira o valor do primeiro lado do triângulo: (em cm): "))
b = float(input("Insira o valor do segundo lado do triângulo: (em cm ):"))
c = float(input("Insira o valor do terceiro lado do triângulo: (em cm): "))

s = float(a + b + c)/2

area_triangulo = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("A Área do triângulo equivale a:(em cm) ", area_triangulo)
