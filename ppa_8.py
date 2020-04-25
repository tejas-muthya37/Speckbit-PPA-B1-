name = input("ENTER YOUR NAME : ")
result = [i for i in name if i.isalpha() or i.isspace()]
result1 = "".join(result)
print(result)
print(result1)