# 定義複利率本利和計算函式
def calculate_compound_interest(principal, annual_rate, years):
    # 將百分比年利率轉換為小數（例如：2.2% -> 0.022）
    rate = annual_rate / 100
    # 套用公式：本利和 = 本金 * (1 + 年利率/12)**(12 * n)
    total_amount = principal * ((1 + rate / 12) ** (12 * years))
    return total_amount

# 主程式
print("== 複利率本利和試算 ==")

# 接收使用者輸入
principal = float(input("請輸入本金："))
annual_rate = float(input("請輸入年利率(%)："))
years = int(input("幾年後領回："))

# 呼叫函式計算結果
total = calculate_compound_interest(principal, annual_rate, years)

# 印出結果（按圖片範例格式，結果保留適當小數）
print()
print(f"*** {years} 年後領回本利和：{total:.1f} ***")