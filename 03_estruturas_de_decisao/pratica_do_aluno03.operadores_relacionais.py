media_aluno=float(input("Digite a media do aluno"))
frequencia_percentual=float(input("Digite a frequencia (%)"))
aprovado= media_aluno >= 6 and frequencia_percentual >= 75
print (f"status de aprovação:{aprovado}")