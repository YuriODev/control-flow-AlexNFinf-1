# Your solution to Exercise 17
ticketnum = int(input("Numbers "))
num1 = ticketnum // 100000
num2 = ticketnum // 10000 % 10
num3 = ticketnum // 1000 % 10
num4 = ticketnum // 100 % 10
num5 = ticketnum // 10 % 10
num6 = ticketnum % 10

if num1 + num2 + num3 == num4 + num5 + num6:
  print("Happy")
else:
    print("Ordinary")

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)