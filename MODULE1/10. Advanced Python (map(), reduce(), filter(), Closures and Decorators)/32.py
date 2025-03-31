# Write a Python program that filters out even numbers using the filter() function. 

l1 = [23,40,20,10,65,100]

l2 = list(filter(lambda n:n%2==0,l1))
    
print(l2)