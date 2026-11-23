"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
matricula=int(input("Escolha a opção correspondente: 1-programador, 2-marketing, 3-designer: "))
match matricula:
    case 1:
        print("Parabéns! você escolheu programador")
    case 2:
        print("Parabéns! você escolheu marketing")
    case 3:
        print("Parabéns! você escolheu designer")

dicionario={
    "cargo", matricula
}
print(dicionario)