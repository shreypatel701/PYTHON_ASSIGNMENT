List1 = ['apple', 'banana', 'mango']

search_string = 'banana'


found = False

for fruit in List1:
    if fruit == search_string:
        found = True
        break

if found:
    print(f"The string '{search_string}' is found in the list.")
else:
    print(f"The string '{search_string}' is not found in the list.")
