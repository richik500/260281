l=[3,7,10,20,4,1,6,8]
for i in range(0,len(l)-1,2):
    t=l[i]
    l[i]=l[i+1]
    l[i+1]=t
print(l)