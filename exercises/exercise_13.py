# Your solution to Exercise 13
natnum = int(input("4 digit"))
digit1 = natnum // 1000 #1
digit2 = (natnum // 100) %10 #2
digit3 = (natnum // 10) %10 #3
digit4 = (natnum %10) #4
if digit1 == digit2:
    output = "False"
elif digit2 == digit3:
    output = "False"
elif digit3 == digit4:
    output = "False"
elif digit1 == digit3:
    output = "False"
elif digit1 == digit4:
    output = "False"
elif digit2 == digit4:
    output = "False"
else:
    output = "True"

print(output)
