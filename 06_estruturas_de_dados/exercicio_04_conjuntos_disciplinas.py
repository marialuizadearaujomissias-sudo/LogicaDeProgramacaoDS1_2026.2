"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web=set(input("Quais são os alunos web? ").split(","))
alunos_banco=set(input("Quais são os alunos banco?").split(","))

intersecao=alunos_banco & alunos_banco
diferenca=alunos_banco - alunos_web

print(f"Os alunos que estão nas duas materias ao mesmo tempo são:{intersecao} ")
print(f"Os alunos que não estão nas duas materias ao mesmo tempo são:{diferenca}")