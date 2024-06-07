output = ""
# Your solution to Exercise 14
natnum = int(input("4 digit"))
digit1 = natnum // 1000 #1
digit2 = (natnum // 100) %10 #2
digit3 = (natnum // 10) %10 #3
digit4 = natnum %10 #4
num = str(digit1) + str(digit2)
num2 = str(digit4) + str(digit3)

if digit1 == digit4 and digit2 == digit3:
    output = "True"
else:
    output = "False"
print(output)