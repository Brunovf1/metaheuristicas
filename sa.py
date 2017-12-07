import math
import random
import pylab


def neighbor(value):
    delta = random.random()
    if random.random() > 0.5:
        return value + delta
    else:
        return value - delta


def fitness(value):
    if value == 0:
        value = 0.000001
    return -2 * math.sin(value / math.pi) / value


def main():
    b = 10  # initial solution
    k = 0  # temperature change counter
    T = 10  # inital temperature
    mk = 30  # number of repetitions
    temp = T
    while temp > 1:
        for i in range(1, mk):
            w = neighbor(b)
            delta = fitness(w) - fitness(b)
            # print("delta: " + str(delta))
            if(delta <= 0):
                b = w
            elif(delta > 0):
                # print(math.e ** (-delta / temp))
                if(random.random() > math.e ** (delta / temp)):
                    b = w
        temp = temp * .9
        k += 1


if __name__ == '__main__':
    pylab.plt
    main()
