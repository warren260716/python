name = ["老張", "發叔", "李董", "豪哥", "小何"]
age = [54, 46, 50, 40, 38]

data = [(age[i], name[i]) for i in range(len(age))]

choice = input("1. 由小到大排序  2. 由大到小排序：")

if choice == "1":
    data.sort(reverse=False) 
    print("由小到大排序：", end="  ")
elif choice == "2":
    data.sort(reverse=True) 
    print("由大到小排序：", end="  ")

for age, name in data:
    print(f"{name}:{age}", end="  ")
print()