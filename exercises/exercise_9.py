# Your solution to Exercise 9
dig3 = int(input("Enter a 3 digit integer: "))
dig1 = dig3 // 100
dig2 = dig3 // 10 % 10
dig3 = dig3 % 10
if (dig1 + dig3) == dig2:
    output = "="
elif (dig1 + dig3) > dig2:
    output = ">"
elif (dig1 + dig3) < dig2:
    output = "<"
print(output)
