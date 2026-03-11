day = int(input())
month = int(input())
year = int(input())

# Check leap year
leap = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True

# Days in months
if month in [1,3,5,7,8,10,12]:
    max_day = 31
elif month in [4,6,9,11]:
    max_day = 30
elif month == 2:
    if leap:
        max_day = 29
    else:
        max_day = 28
else:
    print("Invalid Date")
    exit()

# Validate day
if day < 1 or day > max_day or year <= 0:
    print("Invalid Date")
else:
    day += 1

    if day > max_day:
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    print(f"{day:02d}-{month:02d}-{year}")