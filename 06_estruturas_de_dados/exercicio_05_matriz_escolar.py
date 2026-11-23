"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
matriz=[
    ["Ana", 7.0, 10.0],
    ["Bruno", 6.0, 8.0],
    ["Carla", 10.0, 9.0]
]
for aluno in matriz:
    nome=aluno[0]
    nota1=aluno[1]
    nota2=aluno[2]
    media = (nota1 + nota2) / 2
if media >= 6.0:
    situacao="O aluno esta aprovado"
else:
    situacao="Prova Final"
print(f"Aluno:{nome}| Media:{media}| Situacao: {situacao}")