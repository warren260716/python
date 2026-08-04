while True:
    print("=== 主功能表 ===")
    print("1. 新增作業")
    print("2. 修改作業")
    print("3. 查詢作業")
    print("0. 結束程式")

    choice = input("請輸入選項(0 ~ 3) : ")

    if choice == "1":
        print("1.新增作業")
        input("按 Enter 鍵回到主選單...") 
        print()
    elif choice == "2":
        print("2.修改作業")
        input("按 Enter 鍵回到主選單...") 
        print()
    elif choice == "3":
        print("3.查詢作業")
        input("按 Enter 鍵回到主選單...") 
        print()
    elif choice == "0":
        print("結束程式！")
        break
    else:
        print("輸入值不正確")
        input("按 Enter 鍵回到主選單...")
        print()
        