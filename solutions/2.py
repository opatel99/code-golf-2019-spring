while 1:
 x=input().split()
 if len(x)<1:break
 a,b=map(int,x);print(bin(a^b).count('1'))