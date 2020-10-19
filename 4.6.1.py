from sys import argv
from itertools import count
scr_n, num, stop = argv

def my_f(n):
    for el in count(int(n)):
        yield el
i = 0
while True:
    if i < int(stop):
        print(next(my_f(num)))
        i += 1
