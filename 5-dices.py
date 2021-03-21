import random
import matplotlib.pyplot as plt

random.seed(123)

def roll_dices():
    return random.randrange(6) == random.randrange(6)

def play(reward):
    vezes_lancadas = 0

    while(True):
        vezes_lancadas += 1
        if roll_dices():
            break

    return reward - vezes_lancadas


def main(plays, reward, filename):

    lucro_ou_nao = 0
    lista = []
    for i in range(plays):
        lucro_ou_nao += play(reward)
        lista.append(lucro_ou_nao)

    plt.plot(lista)
    plt.axhline(y=0, color="r", linestyle="-")
    plt.xlabel("Plays")
    plt.ylabel("Lucro ou não")
    plt.savefig(filename)

if __name__ == "__main__":

    plays = 100
    reward = 6
    filename = "imgs/dices.png"

    main(plays, reward, filename)