import time
import sys

Lyrics = [
    ("E tudo que eu posso te dar é solidão com vista pro mar, ou outra coisa pra lembrar", "00:010"),
    ("Às vezes eu quero demais, mas nunca sei se eu mereço", "00:05"),
    ("Os quartos escuros pulsam e pedem por nós", "00:05"),
    ("E tudo que eu posso te dar é solidão com vista pro mar, ou outra coisa pra lembrar", "00:10"),
    ("Se você quiser, eu posso tentar, mas", "00:11"),
    ("Eu não sei dançar tão devagar", "00:11"),
    ("Pra te acompanhar", "00:03")
]

for frase, tempo in Lyrics:
    print(tempo, "-", frase)