from functools import reduce
n = 20
for i in range(n, reduce(lambda x, y: x*y, list(range(1, 21)))+1, n):
    if sum([i%n for n in range(1,21)]) == 0:
        break
print(i)

# Lazy solution - Redo later with research?
