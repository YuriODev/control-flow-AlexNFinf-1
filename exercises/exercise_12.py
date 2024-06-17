# Your solution to Exercise 12
digit4num = int(input("4 digit number: ")) #1234
digit1 = digit4num // 1000 #1
digit2 = (digit4num // 100) %10 #2
digit3 = (digit4num // 10) %10 #3
digit4 = (digit4num %10) #4
if digit1 %2 == 0: #EVEN
    digit1 = "*"
if digit2 %2 == 0: #EVEN
    digit2 = "*"
if digit3 %2 == 0: #EVEN
    digit3 = "*"
if digit4 %2 == 0: #EVEN
    digit4 = "*"
num = str(digit1)
num2 = str(digit2)
num3 = str(digit3)
num4 = str(digit4)

print(f"{num}{num2}{num3}{num4}")