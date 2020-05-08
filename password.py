alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "$#@"
password = input("Enter your password : ")
j = 0
k = 0
l = 0
m = 0
if len(password) >= 8 and len(password) <= 16:
	for i in password:
		if i in alphabets:
			j += 1
		elif i in alphabets1:
			k += 1
		elif i in numbers:
			l += 1
		elif i in special:
			m += 1
if (j >= 1) and (k >= 1) and (l >= 1) and (m >= 1):
	print("Valid Password")
else:
	print("Invalid Password")

	
	



