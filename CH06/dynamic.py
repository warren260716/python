lst = []
# 計算輸入字元總長度
count = eval(input('請輸入lst串列的元素數量：'))
print('請依序填入各元素的內容...')
# 會產生一個從 0 開始、長度為 count 的數字序列
for i in range(count):
    print(f'輸入第{i+1}個元素內容：', end = '')
    num = eval(input())
    lst.append(num)

print('lst串列的元素內容：')
for x in lst:
    print(x, end = ' ')