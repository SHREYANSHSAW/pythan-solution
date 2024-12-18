num = int (input("hey, give your no. to know factorial"))

fact = 1

if num <0:
    print("factorial doesnot exist",)

if num ==0:
    print("your fact is 0")

for i in range(1,num+1):
    fact = fact*i
    print("your factorial is",fact)
