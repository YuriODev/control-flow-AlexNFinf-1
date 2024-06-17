# Your solution to Exercise 8
num1 = int(input("Number: "))
num2 = int(input("Special Number: "))

first = num1 // 100
second = num1 // 10 % 10
third = num1 % 10
if num2 == first or num2 == second or num2 == third:
    print(True)
else:
    print(False)