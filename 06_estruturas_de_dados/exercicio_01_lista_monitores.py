"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:
monitores=["Ryan Mesquita Damasco"]
n1=(input("Digite o primeiro monitor: "))
monitores.append(n1)
n2=(input("Digite o segundo monitor: "))
monitores.append(n2)
monitores[0]="Maria Luiza"
print(monitores)