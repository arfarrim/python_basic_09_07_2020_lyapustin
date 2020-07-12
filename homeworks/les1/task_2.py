#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.
time_sec_summ = int(input("введите время в секундах"))
time_hh = time_sec_summ // 3600
time_mm = (time_sec_summ % 3600) // 60
time_ss = time_sec_summ - time_hh * 3600 - time_mm * 60
print(f"форматированное время - {time_hh}:{time_mm}:{time_ss}")