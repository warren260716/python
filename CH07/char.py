print(chr(65))  # A
print(chr(97))  # a
print(chr(48))  # 0
print(chr(21488))  # 台
print(chr(128522))  # 😊

alphabet = [chr(i) for i in range(65, 91)]  # A-Z
print(alphabet)

char = 'C'
shift = 3
new_char = chr((ord(char) +shift))
print(f"'{char}'向後推{shift}位是：'{new_char}'")