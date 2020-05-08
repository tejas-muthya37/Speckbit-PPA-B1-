str1 = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
list_1 = str1.split(" ")
list_1.sort()
dict1 = {}
for i in list_1:
	dict1[i] = list_1.count(i)
list1 = []
list1.append(dict1)
list2 = []
for i in range(len(list1)):
	if list1[i] not in list1[i + 1:]:
		list2.append(list1[i])
for i in list2:
	for key, val in i.items():
		print(key, ":", val)	