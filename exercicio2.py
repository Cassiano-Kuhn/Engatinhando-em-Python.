# utilizar o random em um jogo de cara e coroa, saber se ganhou ou perdeu.

import random

quer = input("Quer jogar? S/N ").upper()

# validação
while quer != "S" and quer != "N":
    quer = input("Escreva S/N se quiser jogar: ").upper()

if quer == "S":

    caco_escolha = input("Quer cara ou coroa? 1 - Cara | 2 - Coroa: ")

    while caco_escolha != "1" and caco_escolha != "2":
        caco_escolha = input("Digite apenas 1 ou 2: ")

    # sorteio da moeda
    moeda = random.randint(1, 2)

    if moeda == 1:
        resultado = "cara"
    else:
        resultado = "coroa"

    print(f"Deu {resultado.upper()}!")

    if (caco_escolha == "1" and resultado == "cara") or \
       (caco_escolha == "2" and resultado == "coroa"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

elif quer == "N":
    print("Que pena ;-;")
