# Your solution to Exercise 7
num1 = float(input("Number: "))
num2 = float(input("Number: "))
operation = input("Operation: ")

if operation == "+":
    output = num1 + num2
elif operation == "x" or operation == "*":
    output = num1 * num2
elif operation == "/":
    if num2 == 0:
        output = "Division by 0!"
    else:
        output = num1 / num2
elif operation == "-":
    output = num1 - num2

print(output)