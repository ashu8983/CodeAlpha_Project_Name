
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibo(n-2) + fibo(n-1))


n=int(input("Enter number of terms: "))
for i in range(1,n+1):
    print(fibo(i))

