#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
while True:
    base_num = input("введите целое положительное число")
    if base_num.isdecimal() == True:
        break
i = 1
max = int(base_num[0])
while i < len(base_num):
    if int(base_num[i]) > max:
        max = int(base_num[i])
    i += 1
print("максимальная цифра в введенном числе - ", max)

