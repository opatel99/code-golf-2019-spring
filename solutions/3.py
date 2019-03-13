while 1:
 s=input()
 if len(s)<1:break
 l=t=s[0]
 for c in s[1:]:
  t=c if c<t[-1] else t+c
  if len(t)>len(l):l=t
 print(l)