Data = [
    ["老張", "0911443300"],
    ["Mary", "0928000001"],
    ["發叔", "0431748484"],
    ["Tom", "0912345678"],
    ["李董", "0255111111"],
    ["豪哥", "0977229000"],
    ["小何", "0928888888"],
]

name = input("輸入查詢的姓名：")

for person in Data:
    if person[0] == name:
        print(f"{name} 的電話號碼為 {person[1]}")
        break
else:
    print(f"查無 {name} 的資料")