t=(1,2,2,34,4,4,4,47)
s=set()
repeat=set()
for i in t:
    if s.__contains__(i):
        repeat.add(i)
    else:
        s.add(i)
for i in repeat:
    print(i)