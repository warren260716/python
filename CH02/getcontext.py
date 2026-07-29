import decimal
d1=decimal.Decimal.from_float(123.4567) #把浮點資料轉成decimal
d2=decimal.Decimal.from_float(34.5678) #把浮點資料轉成decimal
print(d1+d2)

print(decimal.getcontext()) #取出目前decimal資料型別運算的設定值
print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)
decimal.getcontext().prec=8
print(d1+d2)
