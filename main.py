import reg
from reg import add_part, see_part
print("___________________________________________________________\n")
print("Welcome to Registrant Manager :)")
print("___________________________________________________________\n")
while True:
	choice = input("What would you like to do?\n\n1. Add Participant \n2. See Participants\n3. Exit\n\n")
	if choice == "1":
		add_part()
	elif choice == "2":
		see_part()
	else:
		break
	