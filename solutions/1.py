n=3
while n<1e5:
 n+=2
 if all(n%i&~2for i in range(2,n-2)):print(n-2, n)