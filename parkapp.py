import time
start_time = time.time()
class Parking:
	two_wheeler_slots = int(input("Enter the number of 2 Wheeler slots available : "))
	four_wheeler_slots = int(input("Enter the number of 4 Wheeler slots available : "))
	def __init__(self):
		pass

	def enter(self):
		choice = input("What type of a vehicle is entering?\n\t1. 2 Wheeler\n\t2. 4 Wheeler\n\t")
		if choice == "1":
			self.two_wheeler_slots = self.two_wheeler_slots - 1
			print("Slots : ", self.two_wheeler_slots)
			

		elif choice == "2":
			self.four_wheeler_slots = self.four_wheeler_slots - 1
			print("Slots : ", self.four_wheeler_slots)
			

	def exit(self):
		type = input("What type of a vehicle is exiting?\n\t1. 2 Wheeler\n\t2. 4 Wheeler\n\t")
		if type == "1":
			self.two_wheeler_slots = self.two_wheeler_slots + 1
			print("Slots : ", self.two_wheeler_slots)
			stop_time_2 = (time.time() - start_time)*900
			if stop_time_2 > 3600 and stop_time_2 <= 7200:
				print("Parking Fee : 30 ₹")
			elif stop_time_2 > 7200 and stop_time_2 <= 10800:
				print("Parking Fee : 40 ₹")
			elif stop_time_2 > 10800 and stop_time_2 <= 14400:
				print("Parking Fee : 50 ₹")
			else:
				print("Parking Fee : 70 ₹")

		elif type == "2":
			self.four_wheeler_slots = self.four_wheeler_slots + 1
			print("Slots : ", self.four_wheeler_slots)
			stop_time_4 = (time.time() - start_time)*900
			if stop_time_4 > 3600 and stop_time_4 <= 7200:
				print("Parking Fee : 50 ₹")
			elif stop_time_4 > 7200 and stop_time_4 <= 10800:
				print("Parking Fee : 60 ₹")
			elif stop_time_4 > 10800 and stop_time_4 <= 14400:
				print("Parking Fee : 70 ₹")
			else:
				print("Parking Fee : 100 ₹")

	def show_slots(self):
		print("4 Wheeler Slots : ", self.four_wheeler_slots, "\n2 Wheeler Slots : ", self.two_wheeler_slots)


print("____________________________________________________________")
print("\nWelcome to ParkPal :)")
print("____________________________________________________________")
while True:
	choice = input("Choose from the options below :-\n\t 1. Vehicle Entering\n\t 2. Vehicle Exit\n\t 3. Show available slots\n")
	if choice == "1":
		vehicle_no = input("Enter the vehicle number : ")
		vehicle = Parking()
		vehicle.enter()
	elif choice == "2":
		vehicle.exit()
		del vehicle
	elif choice == "3":
		vehicle.show_slots()
	else:
		break	  



