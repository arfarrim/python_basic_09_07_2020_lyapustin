#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
base_num = input("введите число n")
num_1 = int(base_num)
num_2 = int(base_num + base_num)
num_3 = int(base_num + base_num + base_num)
answer = num_1 + num_2 + num_3
print(answer)
