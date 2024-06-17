# Your solution to Exercise 3
number = int(input("Enter a number: "))
if 1 <= number <= 10:
    if number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif number >= 11 and number < 19:
    if number %2 == 0:
        print("Red")
    else:
        print("Black")
elif number >= 19 and number <= 28:
    if number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif number >= 29 and number <= 36:
    if number %2 == 0:
        print("Red")
    else:
        print("Black")
elif number == 0:
    print("Green")
else:
    print("The bet will not play!")