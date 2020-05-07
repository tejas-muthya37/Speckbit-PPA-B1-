to_do = []
done = []
class To_do:

	def __init__(self):
		pass

	def add(self):
		self.task = input("\tWrite down the task that has to be completed : ")
		to_do.append(self.task)

	def mark_done(self):
		self.done = input("\tThe task that has been completed is : ")
		to_do.remove(self.done)
		done.append(self.done)

	def see_tasks(self):
		print("\n", name + " has to - ", to_do, "\n", name + " has done - ", done) 

print("__________________________________________\n")
print("Welcome to TaskX :)")
print("__________________________________________\n")
name = input("How would you like TaskX to address you?\n")
print("__________________________________________\n")
print("Hey " + name + " !\n\t")
list_name = input("\nEnter the name of your to-do list : ")
while True :
	choice = input("\n\nWhat would you like to do?\n\t1. Add a task. 2. Mark a task as done. 3. See the remaining and completed tasks.\n\t")
	if choice == "1":
		p1 = To_do()
		p1.add()
	elif choice == "2":
		p1.mark_done()
	elif choice == "3":
		p1.see_tasks()
	else:
		 break