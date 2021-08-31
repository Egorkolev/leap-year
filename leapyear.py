# Leap Year

year = int (input("Введите год :"))
if year % 4 != 0:
    print("Не Високосный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Не Високосный")
else:
    print("Високосный")
