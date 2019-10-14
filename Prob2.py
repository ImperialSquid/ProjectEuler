lst = [1, 2]
while lst[len(lst)-1] < 4000000:
    lst.append(lst[len(lst)-1]+lst[len(lst)-2])

print(sum([x for x in lst if x%2 == 0]))
