l = int(input("Enter the no of arrays needed : "))
m = int(input("Enter height of every list : "))
n = int(input("Enter width of every list : "))
ar = []
for i in range(l):
	jList = []
	for j in range(m):
		kList = []
		for k in range(n):
			kList.append("*")
		jList.append(kList)
	ar.append(jList)
print(str(ar).replace("'","").replace("],","],\n"))

