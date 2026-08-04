lst = [[i * j for j in range(1, 10)] for i in range(1, 10)]

for row in lst:
    for num in row:
        print(f"{num:3d}", end="")
    print() 