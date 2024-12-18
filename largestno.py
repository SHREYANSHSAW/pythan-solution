num1 = float(input("enter your no."))
num2 = float(input("enter your 2nd number"))
num3 = float(input ("enter your another no."))

if (num1 > num2) & (num2 > num3):
    print ("num1 is largest number", num1)
elif(num2 >num3) & (num3 > num1):
    print("then num2 is largest no.", num2)
else:
    print("num3 is largest no.", num3)   