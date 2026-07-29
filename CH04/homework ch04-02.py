income = float(input("請輸入年收入（萬元）："))
# 判斷稅率並計算稅額
if income <= 54:
    tax_rate = 0
    tax = 0
    print(f"年收入 {income:.2f} 萬元，稅率 {tax_rate}%，應納稅額 {tax:.2f} 萬元")
elif income <= 121:
    tax_rate = 12
    tax = income * 0.12
    print(f"年收入 {income:.2f} 萬元，稅率 {tax_rate}%，應納稅額 {tax:.2f} 萬元")
elif income <= 242:
    tax_rate = 20
    tax = income * 0.20
    print(f"年收入 {income:.2f} 萬元，稅率 {tax_rate}%，應納稅額 {tax:.2f} 萬元")
elif income <= 453:
    tax_rate = 30
    tax = income * 0.30
    print(f"年收入 {income:.2f} 萬元，稅率 {tax_rate}%，應納稅額 {tax:.2f} 萬元")
elif income <= 1031:
    tax_rate = 40
    tax = income * 0.40
    print(f"年收入 {income:.2f} 萬元，稅率 {tax_rate}%，應納稅額 {tax:.2f} 萬元")
else:  # 大於1031萬
    tax_rate = 45
    tax = income * 0.45
    print(f"年收入 {income:.2f} 萬元，稅率 {tax_rate}%，應納稅額 {tax:.2f} 萬元")