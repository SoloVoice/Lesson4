from itertools import cycle


def my_f(lst):
    for el in cycle(lst):
        if el <= len(lst):
            yield el


my_list = [el for el in range(20, 31)]
for i in my_f(my_list):
    print(i)

"""for el in cycle(my_list):
    if c >= len(my_list):
        break
    print(el)"""