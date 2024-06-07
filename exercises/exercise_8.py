# Your solution to Exercise 8
num1 = int(input("Number: "))
num2 = int(input("Special Number: "))
contain = num1 == num2 % 10 or num1 == (num2 // 10) % 10 or num1 == num2 // 100
print(contain)