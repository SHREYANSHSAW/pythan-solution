lower1 = int(input("input your lower number to get prime no."))
upper2 = int(input("your last number"))

for num in range (lower1,upper2+1):
    if num > 1 :
        for i in range (2, num):
             if num % i == 0:
              break

    else:
        print("your no. is prime", num) 