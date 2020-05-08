list1 = []
n = int(input("Enter the number of elements required in your list : "))
for i in range(0, n):
	n = int(input("Enter the element : "))
	list1.append(n)
print(list1)
num = int(input("Enter the N of your Nth : "))
list1.sort(reverse = True)
i = 0
while i < num - 1:
	list1.pop()
	i += 1
print(list1[-1])

