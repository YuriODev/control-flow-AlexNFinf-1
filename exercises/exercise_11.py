# Your solution to Exercise 11
year = int(input("Year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year.")
else:
    print("Ordinary year.")