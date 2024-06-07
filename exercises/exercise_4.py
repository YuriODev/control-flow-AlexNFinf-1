# Your solution to Exercise 4
grade = int(input("Grade: "))
if grade <= 3:
    output = "initial level"
elif grade >= 4 and grade <=6:
    output = "average level"
elif grade >= 7 and grade <= 9:
    output = "sufficient level"
elif grade >= 10 and grade <= 12:
    output = "high level"
else:
    output = "level is absent"
print(output)