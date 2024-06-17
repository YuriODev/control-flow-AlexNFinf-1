# Your solution to Exercise 15
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
if month == 2:
    if leap_year == True:
        if day >= 29:
            month+=1
            day = 1
        else:
            day+=1
    elif leap_year == False:
        if day > 28:
            month+=1
            day = 1
        else:
            day+=1
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day >= 31:
        month+=1
        day = 1
    else:
        day+=1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 30:
        month+=1
        day = 1
    elif day <30:
        day+=1
elif day == 31 and month == 12:
    day = 1
    month = 1
    year+=1
else:
    print("Invalid Input")
print(f"{day}.{month}.{year}")