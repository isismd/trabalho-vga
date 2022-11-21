# Determinar equações paramétricas da reta r que passa por um determinado ponto A(3, 4, -1) e é ortogonal às retas r1: (x y, z) = (0, 0, 1) + t(2, 3, -4) e r2: (x = 5, y = t, z = 1 - t)

from sympy import pprint, Matrix, symbols
from sympy.parsing.sympy_parser import parse_expr

i, j, k, t = symbols('i j k t')

ponto_A = []
reta_r1 = []
reta_r2 = []
vetor_v1 = []
vetor_v2 = []
reta_r = []

print("======== Digite os 3 valores do ponto A ========")
for indice in range (0, 3):
    ponto_A.append(parse_expr(input()))

print("\n\n======== Digite os valores de x, y e z em t na reta R1 ========")
for indice in range (0, 3):
    reta_r1.append(parse_expr(input()))

print("\n\n======== Digite os valores de x, y e z na reta R2 ========")
for indice in range (0, 3):
    reta_r2.append(parse_expr(input()))

# criando o vetor 1 com base na reta 1
vetor_v1 = reta_r1

# criando o vetor 2 com base na reta 2
for value in reta_r2:
    if isinstance(value, int) is False:
        vetor_v2.append(value.coeff(t))
    else:
        vetor_v2.append(0)

# fazendo o produto escalar
matriz = Matrix([[i, j, k], vetor_v1, vetor_v2])
determinante = matriz.det()
vetor_v3, temp =  zip(*[indice.as_coeff_Mul() for indice in determinante.args])  # type: ignore

# mostrando a matriz e o determinante na tela
print("\nMatriz\n")
pprint(matriz)
print("Determinante = ", determinante)

# criando a reta r
for indice in range(0, 3):
    if vetor_v3[indice] > 0:
        reta_r.append(str(ponto_A[indice]) +" + "+ str(vetor_v3[indice]) +"t")
    else:
        reta_r.append(str(ponto_A[indice]) +" - "+ str(vetor_v3[indice] * -1) +"t")

print("\nReta r = ", reta_r)

# mostrando as equações paramétricas da reta r
print("\nAs equações paramétricas da reta r são: \nx = ", str(reta_r[0]), "\ny = ", str(reta_r[1]), " \nz = ", str(reta_r[2]))
