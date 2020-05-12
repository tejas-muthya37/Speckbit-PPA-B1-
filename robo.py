# import turtle
x = 0
y = 0
from math import sqrt, ceil
print("______________________________________________")
print("Welcome to Robo Tracker! :)")
print("______________________________________________")
print("Please enter all the previous movements of the robot known to you! ;)")
ip = input("Enter your input : ")
list1 = ip.split()
tuple1 = tuple(list1)
print(tuple1)

def turt(tuple):
	global x
	global y

	if tuple[0] == "UP":
		x += int(tuple[1])
		# turtle.forward(int(tuple[1]))
	elif tuple[0] == "DOWN":
		x -= int(tuple[1])
		# turtle.backward(int(tuple[1]))
	elif tuple[0] == "LEFT":
		y -= int(tuple[1])
		# turtle.left(int(tuple[1]))
	elif tuple[0] == "RIGHT":
		y += int(tuple[1])
		# turtle.right(int(tuple[1]))

turt(tuple1)
turt(tuple2)
turt(tuple3)
turt(tuple4)

ip = input("Enter your input : ")
list2= ip.split()
tuple2 = tuple(list2)
print(tuple2)

ip = input("Enter your input : ")
list3 = ip.split()
tuple3 = tuple(list3)
print(tuple3)

ip = input("Enter your input : ")
list4 = ip.split()
tuple4 = tuple(list4)
print(tuple4)

print(x, y)
print("\n\tWe got him! :D ")
dist = sqrt((x**2) + (y**2))
print("\n\tHe's found to be", ceil(sqrt(dist)), "units from home!")

# print("\n\tHe's found to be ", turtle.distance(0, 0), " units from home!")

