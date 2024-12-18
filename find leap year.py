year = int(input("tocheck your birthday is leap year not"))

if (year % 400 == 0) and (year % 100 == 0):
    print(year,"your birthday is in leap year")

elif (year % 4 == 0) and (year % 100 != 0): 
    print(year, "you are in leap year", )

else:
    print(year,"you are not in leap yaer",)    
    