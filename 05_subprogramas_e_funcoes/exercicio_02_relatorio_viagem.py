"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:

def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litros = distancia_km / consumo_kml
    custo = litros * preco_combustivel
    return custo


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo = qtd_pessoas * dias * diaria_alimentacao
    return custo
distancia=float(input("Digite a distancia percorrida: "))
consumo=float(input("Digite o consumo em km/l: "))
preco=float(input("Digite o preco do combustivel: "))
resultado= calcular_custo_transporte (distancia, preco, consumo)
print(resultado)