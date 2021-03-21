import random
import matplotlib.pyplot as plt

random.seed(123)


def play(doors, prize):

    random.shuffle(doors)

    player_choice = random.randrange(len(doors))

    # print(player_choice, doors)

    return doors[player_choice] == prize


def main(plays, doors, prize, filename):

    stick_wins, switch_win_probability, stick_win_probability = 0, [], []

    for i in range(plays):

        if play(doors, prize):
            stick_wins += 1

        stick_win_probability.append(stick_wins / (i + 1))
        switch_win_probability.append((i + 1 - stick_wins) / (i + 1))

        plt.plot(switch_win_probability)
        # plt.plot(stick_win_probability)

    print("Prob. of victory if player always switch: ", switch_win_probability[-1])
    print("Prob. of victory if player always stick to the original choice:", stick_win_probability[-1])

    plt.axhline(y=0.5, color="r", linestyle="-")
    plt.axhline(y=0.66666, color="r", linestyle="-")
    plt.axhline(y=0.33333, color="g", linestyle="-")

    plt.savefig(filename)


if __name__ == "__main__":

    plays = 1000
    prize = "car"
    doors = ["goat", "goat", prize]
    filename = "imgs/monty_hall_problem.png"

    main(plays, doors, prize, filename)
