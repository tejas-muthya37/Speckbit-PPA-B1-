part = {}
def add_part():
	name = input("Enter your name : ")
	event = input("Select an event\n1. Counter Strike\n2. PlayerUnknownsBattleGrounds/PUBG\n3. GoogleIt\n4. TreasureHunt\n\n")
	if event == "1":
		part[name] = "Counter Strike"
	elif event == "2":
		part[name] = "PlayerUnknownsBattleGrounds/PUBG"
	elif event == "3":
		part[name] = "GoogleIt"
	elif event == "4":
		part[name] = "TreasureHunt"

def see_part():
	for key, val in part.items():
		print(key, "-", val)