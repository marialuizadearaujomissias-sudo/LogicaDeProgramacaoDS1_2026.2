soma = 0
numero=int(input("Digite um numero inteiro(0 para parar)"))
while numero !=0:
    soma+= numero
    numero=int(input("Digite um numero inteiro(0 para parar)"))
    print(f"a soma de todos os numeros digitados{soma}")