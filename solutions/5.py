while 1:
 x=input()
 if len(x)<1:break
 s=x[0];y=2
 while y<=len(x):
  s=x[:y]+'\n'+s+'\n'+x[:y];y+=1
 print(s)