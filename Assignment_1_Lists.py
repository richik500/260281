l=[4,1,9,10]
min1 = l[0]
for i in l:
    if i < min1:
        min1 = i
for i in l:
    if i != min1:
        min2 = i
        break
for i in l:
    if i != min1:
        if i < min2:
            min2 = i