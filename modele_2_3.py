list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = -1
while list[n] > 0 or list[n] == 0:
    n += 1
    if list[n] != 0 and list[n] > 0:
        print(list[n])
        continue