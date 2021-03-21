import random
import matplotlib.pyplot as plt

random.seed(123)


def random_walk(n):
    x, y = 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])

        x += dx
        y += dy

    return (x, y)


def main(walks, n, walk_lenght_max, filename):

    walks_result = []

    for walk_lenght in range(1, walk_lenght_max):

        no_transport = 0

        for i in range(walks):

            walk = random_walk(walk_lenght)

            distance = abs(walk[0]) + abs(walk[1])

            if distance <= n:
                no_transport += 1

        avg_no_transport = no_transport / walks

        walks_result.append(avg_no_transport)

        print(f"For walk size {walk_lenght} the % of no transport is {avg_no_transport * 100}")

    plt.plot(walks_result)
    plt.axhline(y=0.5, color="r", linestyle="-")
    plt.xlabel("Walk size")
    plt.ylabel("% no transport")
    plt.savefig(filename)


if __name__ == "__main__":

    n = 4

    walks = 2500
    walk_lenght_max = 50
    filename = "imgs/random_walk.png"

    main(walks, n, walk_lenght_max, filename)
