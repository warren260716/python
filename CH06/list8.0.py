lst1 = [10,20,30,40,50]
# num = len(lst1)
# print(str(num)) # 輸出5
print(str(num := len(lst1)))  # 輸出：5（同時變數 num 也成功被賦予 5），Python 3.8 以上版本才支援 := 運算子

# 使用 f-string
print(f"total = {sum(lst1)}") # 輸出：total = 150
big = max(lst1)
print(str(big)) # 輸出：50
# print(f"big = {max(lst1)}")
print(f"small = {min(lst1)}") #輸出：small = 10