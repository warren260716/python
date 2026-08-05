money = 6359
person = 28
print(f'班費剩餘{money}元, 學生有{person}人')
(div, mod) = divmod(money, person) # 計算每人分到的錢和剩餘的錢
print(f'每人均分得{div}元')
print(f'班費仍剩餘{mod}元')
