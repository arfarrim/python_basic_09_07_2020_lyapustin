#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного
# сотрудника.
while True:
    profit = input("введите сумму выручки")
    if profit.isdecimal() == True:
        break
while True:
    expenses = input("введите сумму издержек")
    if expenses.isdecimal() == True:
        break
profit = int(profit)
expenses = int(expenses)
if profit > expenses:
    print("фирма показывает прибыль")
    print("рентабельность - ", (profit - expenses) / profit)
    while True:
        staff = input("укажите количество персонала")
        if staff.isdecimal() == True:
            break
    print("прибыль в расчете на одного сотрудника - ", (profit - expenses) / int(staff))
elif profit == expenses:
    print("вышли в ноль")
else:
    print("фирма работает в убыток")