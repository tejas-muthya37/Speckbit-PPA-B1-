dict_1 = {"hello":"world", "hey":"speckbit", "hi":"python"}
query_name = input("enter your search value : ")
for key, value in dict_1.items():
	if query_name == value:
		print(key)
	