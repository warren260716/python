# 輸入一個1~12之間的整數
month = int(input("請輸入1~12之間的整數："))
# 判斷季節
if month in (3, 4, 5):
    print("春天")
elif month in (6, 7, 8):
    print("夏天")
elif month in (9, 10, 11):
    print("秋天")
elif month in (12, 1, 2):
    print("冬天")
else:
    print("輸入錯誤！")