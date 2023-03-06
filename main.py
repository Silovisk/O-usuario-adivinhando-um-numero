from random import randint


def advinha(x):
    numero_aleatorio = randint(1, x)
    palpite = 0
    while palpite != numero_aleatorio:
        palpite = int(input(f"De um palpite entre 1 e {x} : "))
        if palpite < numero_aleatorio:
            print("Digite um numero maior ")
        elif palpite > numero_aleatorio:
            print("Digite um numero menor")

    print(f"Parabens voce acertou! O numero sorteado era {numero_aleatorio}")


advinha(100)
