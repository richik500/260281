def join(dd1, dd2):
    return dd1.update(dd2)


d1 = {'one': 1, 'two': 2}
d2 = {'three': 3, 'four': 4}
join(d1, d2)
print(d1)
d1 = {'one': 1, 'two': 2}
d2 = {'one': 4, 'four': 4}
join(d1, d2)
print(d1)