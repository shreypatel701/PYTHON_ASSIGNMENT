percentage = int(input("enter the percentage::> "))
if percentage >0 and percentage<100:

    if percentage >= 90 :
        print("A grade")
    elif percentage >=70 and percentage<=80:
        print("B grade")
    elif percentage >=60 and percentage<=70:
        print("c grade")
    elif percentage >=60 and percentage<=50:
        print("D grade")
    elif percentage >=50 and percentage<=40:
        print("E grade")
    else:
        print("fail better luck next time")
else:
    print("invalid number")