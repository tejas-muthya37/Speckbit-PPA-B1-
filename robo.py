import turtle
print("______________________________________________")
print("Welcome to Robo Tracker! :)")
print("______________________________________________")
print("Please enter all the previous movements of the robot known to you! ;)")
ip = input("Enter your input : ")
list1 = ip.split()
tuple1 = tuple(list1)
print(tuple1)

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

def turt(tuple):
	if tuple[0] == "UP":
		turtle.forward(int(tuple[1]))
	elif tuple[0] == "DOWN":
		turtle.backward(int(tuple[1]))
	elif tuple[0] == "LEFT":
		turtle.left(int(tuple[1]))
	elif tuple[0] == "RIGHT":
		turtle.right(int(tuple[1]))

turt(tuple1)
turt(tuple2)
turt(tuple3)
turt(tuple4)
print("\n\tWe got him! :D ")
print("\n\tHe's found to be ", turtle.distance(0, 0), " units from home!")

