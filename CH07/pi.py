import math
# 案例：計算圓形面積與斜邊長
radius = 5.0
circle_area = math.pi * (radius ** 2)
print(f"半徑{radius}的圓面積：{circle_area:.2f}") # 輸出：78.54
# 畢氏定理：計算直角三角形斜邊 (a=3, b=4)
a, b = 3, 4
c = math.sqrt(pow(a,2) + b**2) #pow(a,2) = a**2 = a平方
print(f'斜邊長c:{c}') # 輸出：5.0
