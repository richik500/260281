l = [3, 7, 10, 20]
index=len(l)-1
t={}
for i in range(0,len(l)):
    temp={l[index-i]:t}
    t=temp
print(t)