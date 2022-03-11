s=input()
l=[]
checkBit=int(s[len(s)-1])
for i in range(len(s)-1):
  if(s[i]!=" "):
    l.append(int(s[i]))
sum=0
for i in range(0,len(l)):
  if(i%2==0):
    temp=2*l[i]
    if(temp>=10):
      temp=temp%10+temp//10
      sum+=temp
    else:
      sum+=temp  
  else:
    sum+=l[i]
if((sum+checkBit)%10==0):
  print("original")
else:
  print("fake")