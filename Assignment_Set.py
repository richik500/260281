s={1,1,2,3,4,5,9}
for i in s:
    min=i
    max=i
    break
for i in s:
    if i<min:
        min=i
    if i>max:
        max=i

print(max,min)