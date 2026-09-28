"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input("digite o salario em R$"))
if salario<=2000.00:
    print("isento")
else:
    imposto=0
    if salario >4.500:
        imposto += (salario - 4500.00) * 0.28
        imposto += 1000.00*0.18
        imposto += 1000.00*0.08
    elif salario >3000.00:
        imposto += (salario - 3000.00) * 0.18
        imposto += 1000.00*0.08
    else:
        imposto+= (salario - 2000.00) * 0.4
        print (f"R${imposto:.2f}")