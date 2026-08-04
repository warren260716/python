score = [72, 98, 86, 76, 63]
# 就地修改（In-place）」，它不會回傳任何值
print(f'原始串列：{score}')
score.sort()
print(f'排序後串列:{score}')  # 印出 [63, 72, 76, 86, 98] 
score.reverse()
print(f'反轉後排列：{score}')