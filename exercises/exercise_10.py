# Your solution to Exercise 10
coord1 = int(input("Enter X coord"))
coord2 = int(input("Enter X coord"))
coord3 = int(input("Enter X coord"))
coordy1 = int(input("Enter Y coord"))
coordy2 = int(input("Enter Y coord"))
coordy3 = int(input("Enter Y coord"))




point1 = (coord2-coord1)**2 + (coordy2-coordy1)**2
point2 = (coord3-coord2)**2 + (coordy3-coordy2)**2
point3 = (coord1-coord3)**2 + (coordy1-coordy3)**2
if point1 == 0 or point2 == 0 or point3 == 0:
    print("No")
elif point1 + point2 == point3 or point2 + point3 == point1 or point3 + point1 == point2:
    print("Yes")
else:
    print("No")