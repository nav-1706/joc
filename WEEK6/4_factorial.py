def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

a = int(input("Enter the number you want to find the factorial for: "))
print(fact(a))

## Also write code for Recursive binary search in python