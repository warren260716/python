for x in range(1, 6):
    for y in range(1, 6-x):
       print(' ', end='')
    lst = list(range(x, 0, -1))
    for y in lst:
       print(y, end='')
    print()
print()
