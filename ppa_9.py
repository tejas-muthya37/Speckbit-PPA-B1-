string = "MyReviewOfTheNewPhone:SamsungGalaxyS9"
list1 = []
for i in string:
	if i.isupper():
		list1.append(" " + i)
	else:
		list1.append(i)
string = "".join(list1)
print(string)
	
