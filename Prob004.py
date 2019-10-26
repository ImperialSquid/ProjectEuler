t = 0
for x in range(999, 0, -1):
    for y in range(999, 0, -1):
        if list(str(x*y)) == list(str(x*y))[::-1] and x*y>t:
            t = x*y
print(t)
