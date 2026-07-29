# 顯示選單
print("1. 蘋果")
print("2. 香蕉")
print("3. 芒果")
print()
# 建立中文對應英文的字典
fruit_dict = {
    1: "apple",
    2: "banana",
    3: "mango"
}
# 輸入選項
choice = int(input("請輸入選項<1~3>："))
# 判斷並顯示結果
if choice == 1:
    print(f"英文單字：  {fruit_dict[choice]}")
elif choice == 2:
    print(f"英文單字：  {fruit_dict[choice]}")
elif choice == 3:
    print(f"英文單字：  {fruit_dict[choice]}")
else:
    print("請輸入1~3！")