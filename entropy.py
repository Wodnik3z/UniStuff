import numpy as np
import pandas as pd

print("elo")

vector10 = [4, 5, 6]
vector20 = [1, 1, 3]
char = np.array(['a', 'b', 'c'])
char1 = np.array(['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'd'])
vector = np.random.randint(0, 5, size=10)
rdm = np.random.choice(char, size=10)

print(vector)
print("\n")


def freq(x, prob=True):
    xi = pd.DataFrame(x)
    pi = xi.value_counts()
    if prob == False:

        return pi
    elif prob == True:
        ni = xi.value_counts() / vector.size
        return ni


result = freq(vector, True)

print("\nwyniki zadanie 1\n", result)


def freq2(x, y, prob=True):
    df = pd.DataFrame({'X': x, 'Y': y})
    grup = df.groupby(['X', 'Y']).size()
    n = len(df)

    if prob == False:
        pi = grup
        return pi
    elif prob == True:
        ni = grup / n
        return ni


result1 = freq2(vector, rdm, True)
print("\nwyniki2 zadanie 2\n", result1)


def entropy(x):
    pi = freq(x, True)
    h = 0
    n = len(x)
    for i in range(n):
        h -= pi[x[i]] * np.log2(1 / pi[x[i]])
        # h -= pi * np.log2(1 / pi)
    return h


result2 = entropy(vector10)
print("wynik zad3 entropia\n", result2)


def infogain(x, y):
    pi = freq2(x, y, True)

    hj = 0
    n = len(x)
    for i in range(n):
        hj -= pi[(x[i], y[i])] * np.log2(1 / pi[(x[i], y[i])])
        # h -= pi * np.log2(1 / pi)
    return entropy(x) + entropy(y) - hj  # ????


print("zadanie 3 IG\n", infogain(vector, rdm))  # ?????
xd = pd.read_csv('zoo.csv')
mak = infogain(xd['animal'], xd['hair'])
print("zad 4, przyrost informacji\n", mak)
