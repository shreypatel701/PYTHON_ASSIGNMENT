#  Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("enter the your age::>"))

if age>=18:
    if age>75:
        print("your are not eligible to donate blood")
    else:
        print("your are eligible to donate blood")
else:
    print("your not are eligible to donate blood")