list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([i for x, i in enumerate(list_1) if x != 0 and list_1[x] > list_1[x-1]])
