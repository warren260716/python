import math
print(f'圓周率π：{math.pi}') # 輸出：3.141592653589793
print(f'自然對數 e：{math.e}') # 輸出：2.718281828459045
# 欲儲存 1000 種狀態，至少需要多少個位元 (Bits)？
states = 1000
# 計算公式：ceil(log2(states))，其中 log2 為以 2 為底的對數
bits_needed = math.ceil(math.log(states, 2)) # 計算表示1000個狀態所需的位元數
print(f'儲存{states}種狀態需要：{bits_needed}個位元')  # 輸出：10
# 儲存 1000 種狀態需要 10 個位元