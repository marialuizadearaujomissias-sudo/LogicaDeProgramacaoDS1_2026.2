#TODO: Crie a matriz 2x2 e calcule a soma
matriz = [
    [7, 13],
    [10, 12]
]
soma_total=[0]
for linha in matriz:
    n1=linha[0]
    n2=linha[1]
    soma=(n1+n2)
    print(f"O valor da soma:{soma}")
