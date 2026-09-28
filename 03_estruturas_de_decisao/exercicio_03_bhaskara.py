"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

import math
A = float(input("digite A:"))
B = float(input("Digite B:"))
C = float(input("Digite C:"))

if A == 0:
    print("Impossivel calcular")
else: 
    delta = B**2 - 4*A*C
    R1=(-B+math.sqrt(delta)/(2*A))
    R2=(-B-math.sqrt(delta)/(2*A))
    print(f"R1={R1:.5F}")
    print(f"R2={R2:.5F}")