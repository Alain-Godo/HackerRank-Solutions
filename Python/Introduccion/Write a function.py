def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap

year = int(input())
print(is_leap(year))


# Alternative solution (by mpiele)
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            elif year % 400 != 0:
                leap = False
        elif year % 100 != 0:
            leap = True
    elif year % 4 != 0:
        leap = False

    return leap

year = int(input())
print(is_leap(year))