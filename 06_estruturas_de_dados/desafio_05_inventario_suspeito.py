"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
itens=[
"mouse", "monitor", "teclado"
"cabos", "notebook", "gabinete"
]
itens_unico=set(itens)
print("Lista de itens unicos:", itens)

inventario={
"mouse": 4,
"monitor":4,
"teclado":5,
"cabos":10,
"notebook": 12,
}
print("Quantidade de mouses: ", inventario.get("mouse"))
print("Quantidade de gabinetes: ", inventario.get("item não encontrado"))