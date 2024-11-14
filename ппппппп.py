# 7.1 Списки
import random


def generate():
    a = []
    while len(a) != 10:
        rand = random.randint(1, 100)
        a.append(rand)
    print(a)
    return a


def middle(a):
    mid = sum(a)
    return mid


gen = generate()
av = middle(gen)
print(av)