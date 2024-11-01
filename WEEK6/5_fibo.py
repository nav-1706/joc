def fibo(n):
    if(n < 2) : return n;
    return fibo(n-1) + fibo(n-2);

n = int(input("Enter n to find the nth fibo number: "))
print(fibo(n))