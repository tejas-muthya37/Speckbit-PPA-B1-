students = {"Alex" : {"Math" : "50", "Physics" : "98", "Chemistry" : "69", "Biology" : "78", "Social Science" : "89"}, 
"Steve" : {"Math" : "78", "Physics" : "87", "Chemistry" : "98", "Biology" : "88", "Social Science" : "79"},
"Martin" : {"Math" : "45", "Physics" : "99", "Chemistry" : "100", "Biology" : "89", "Social Science" : "88"}, 
"Trisha" : {"Math" : "66", "Physics" : "68", "Chemistry" : "70", "Biology" : "71", "Social Science" : "68"}}

queries = {"Trisha" : "Math", "Alex" : "Chemistry", "Martin" : "Biology"}

for key in queries:
	out = students[key][queries[key]]
	print(key, "scored", out, "in", queries[key])