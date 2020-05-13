from tabulate import tabulate
cart = {}
def browse():
	categories = input("\nWhich category would you like to browse? :)\n\t1. Apparels\n\t2. Shoes\n\t3. Electronics\n\t4. Educational\n\t")
	if categories == "1":
		apparel = [["Jeans", 38, 1499],["Harry Potter Merchandise", "L", 449],["Yoga Pants", "M", 199]]
		headers = ["Product", "Size", "Price in ₹"]
		print(tabulate(apparel, headers, tablefmt="github"))
		add = input("\n\nWould you like to add anything to your cart?\n\t1. YES!\n\t2. NO!\n\t")
		if add == "1":
			n = input("\nEnter the name of the product you want to add in your cart : ")
			if any(n in a for a in apparel):
				for i in range(len(apparel)):
					if apparel[i][0] == n:
						cart[n] = apparel[i][2]

	elif categories == "2":
		shoe = [["Nike Shoe", 12, 4499],["Flip Flops", "8", 499],["Crocs", "14", 3999]]
		headers = ["Product", "Size", "Price in ₹"]
		print(tabulate(shoe, headers, tablefmt="github"))
		add = input("\n\nWould you like to add anything to your cart?\n\t1. YES!\n\t2. NO!\n\t")
		if add == "1":
			n = input("Enter the name of the product you want to add in your cart : ")
			if any(n in a for a in shoe):
				for i in range(len(shoe)):
					if shoe[i][0] == n:
						cart[n] = shoe[i][2]

	elif categories == "3":
		electronics = [["Samsung Galaxy S9+", "Space Grey", 34999],["Dell Latitude I7 8th Gen", "Pitch Black", 99999],["JBL Headphones", "Ice White", 899]]
		headers = ["Product", "Colour", "Price in ₹"]
		print(tabulate(electronics, headers, tablefmt="github"))
		add = input("\n\nWould you like to add anything to your cart?\n\t1. YES!\n\t2. NO!\n\t")
		if add == "1":
			n = input("Enter the name of the product you want to add in your cart : ")
			if any(n in a for a in electronics):
				for i in range(len(electronics)):
					if electronics[i][0] == n:
						cart[n] = electronics[i][2]

	elif categories == "4":
		educational = [["H.C Verma : Physics", 2018, 699],["There's Nothing Like Enlightenment : U.G. Krishnamurthy", 2014, 1199],["All About Personal Branding", 2017, 499]]
		headers = ["Product", "Published In", "Price in ₹"]
		print(tabulate(educational, headers, tablefmt="github"))
		add = input("\n\nWould you like to add anything to your cart?\n\t1. YES!\n\t2. NO!\n\t")
		if add == "1":
			n = input("Enter the name of the product you want to add in your cart : ")
			if any(n in a for a in educational):
				for i in range(len(educational)):
					if educational[i][0] == n:
						cart[n] = educational[i][2]

def view():
	cart_1 = []
	for key, val in cart.items():
		cart_1.append([key, val])
	headers = ["Products", "Prices"]
	print(tabulate(cart_1, headers, tablefmt="github"))

def checkout():
	total = []
	for key, val in cart.items():
		total.append(val)
	print("\nYour total bill is : ", sum(total))
	print("\n\tFeel free to choose any of our payment methods :)\n\n\tThank you! :) Visit Again.")

print("____________________________________________________________________________")
print("\t\t\t\tWelcome to KAPT! :D ")
print("____________________________________________________________________________")
while True:
	choice = input("\n\nWhat would you like to do? :)\n\t1. Browse Inventory\n\t2. View Cart\n\t3. Checkout\n\t")
	if choice == "1":
		browse()
	elif choice == "2":
		view()
	elif choice == "3":
		checkout()
	else:
		break



 

