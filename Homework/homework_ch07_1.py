def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("輸入第一個正整數 a："))
num2 = int(input("輸入第二個正整數 b："))

result = gcd(num1, num2)

print(f"a, b 兩整數的 GCD 為 {result}")