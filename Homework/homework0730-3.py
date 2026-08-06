choice = input("請選擇單位（1: 公尺轉英尺, 2: 公斤轉英磅）：")

if choice == "1":
    amount = float(input("請輸入數量："))
    print(f"{amount} 公尺 = {amount * 3.28:.6f} 英尺")
elif choice == "2":
    amount = float(input("請輸入數量："))
    print(f"{amount} 公斤 = {amount * 2.2:.6f} 英磅")
else: 
    print("無此選項")