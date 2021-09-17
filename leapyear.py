# Leap Year
l = int(input('Введите год:'))
def leap(l):
    if l % 100 == 0:
        return True
    if l % 400 == 0:
        return True
    if l % 4 != 0:
        return False
    else:
        return True
print(leap(l))





