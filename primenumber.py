#prime = int(input("your no. is prime or not"))

#if prime ==1:
#    print("it is not prime no.")

#if prime > 1:
#    for i in range (2, prime):
#        if prime % i == 0:
#            print("it is not a prime no.", prime)
#            break
#        else:
#           print("it is prime number", prime)


num = int(input("get your is prime or not"))
                                                                                                                                                          
if num ==1:
    print("this number is not prime no.",)
    breakpoint                                                      

    if num > 1:
        for i in range(2, num):
            if num % i ==0:
                print("it is not a prime no", num) 
                break
            else:
                print("it is prime no.", num)