l=[('one',1),('two',2),('three',3)]
d={}
for i in range(0,len(l)):
    temp=l[i]
    dd={temp[0]:temp[1]}
    d.update(dd)
print(d)