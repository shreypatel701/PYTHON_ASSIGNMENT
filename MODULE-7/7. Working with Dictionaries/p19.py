# Write a Python program to merge two lists into one dictionary using a loop. 

my_dict = {}

keys = ["name","marks","subjects"]
value = ["shrey",50,"python"]

for i in range(len(keys)):
    my_dict[keys[i]] = value[i]

print(my_dict)