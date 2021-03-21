import math
import random
import matplotlib.pyplot as plt

random.seed(123)

def atira(raio):
    x = random.random() - 0.5
    y = random.random() - 0.5
    return math.sqrt((x ** 2) + (y ** 2)) < raio

def main(plays,raio,filename):
    acertadas = 0
    lista = []

    for i in range(plays):
        if atira(raio):
            acertadas += 1
        j = i+1
        lista.append(4 * (acertadas/j))

    print(len(lista))

    plt.plot(lista)
    plt.axhline(y=3.14, color="r", linestyle="-")
    plt.xlabel("Plays")
    plt.ylabel("Valor de Pi")
    plt.savefig(filename)

    pi_value = 4 * (acertadas/plays)

    print(pi_value)


if __name__ == "__main__":
    plays = 2500
    raio = 0.5
    filename = "imgs/pi_value.png"

    main(plays,raio,filename)
