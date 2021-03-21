import random
import matplotlib.pyplot as plt

random.seed(123)


def coin_flip():
    return "H" if random.random() < 0.5 else "T"


def play():

    flips, n = 0, 0

    while abs(n) != 3:
        if coin_flip() == "H":
            n += 1
        else:
            n -= 1

        flips += 1

    return flips


def main(plays, reward, filename):

    total_spent, wins = 0, []

    for i in range(plays):

        t = play()
        total_spent += t

        print(f"Flips: {t} \t Ganho: {reward - t}€")

        wins.append((i * reward) - total_spent)

    print(f"Final: {(plays * reward) - total_spent}€")

    plt.plot(wins)
    plt.axhline(y=0.5, color="r", linestyle="-")
    plt.xlabel("Plays")
    plt.ylabel("Wins")
    plt.savefig(filename)


if __name__ == "__main__":

    plays = 200
    reward = 8
    filename = "imgs/coin_flip.png"

    main(plays, reward, filename)
