# Most of the year that can be divided by 4 are leap years, exceptions are the century years unless they are dividesd by 400(example 1600 is a leap year, but 1700 is not)

print("Enter the year to check if leap year or not")
# year = int(input("Enter the year: "))

import random
year = random.randint(1993, 2018)

if(year%400 == 0):
    print(f"{year} is a leap year")
elif(year%100 == 0):
    print(f"{year} is not a leap year")
elif(year%4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")