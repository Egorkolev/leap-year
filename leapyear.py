# Leap Year

year = int (input("Введите год :"))
if year %4 == 0:
    print("Высокосный")
elif year %400 == 0:
    print("Высокосный")
else:
    print("Не Высокосный")
