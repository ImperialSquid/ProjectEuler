def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


collatzChainLens = dict()

for i in range(1, 1000001):
    target = i
    collatzChainLens[i] = 1
    while target != 1:
        target = collatz(target)
        if target in collatzChainLens.keys():
            collatzChainLens[i] += collatzChainLens.get(target)
            break
        else:
            collatzChainLens[i] = collatzChainLens.get(i) + 1
    print(i, collatzChainLens.get(i))

longestChain = 0
longestStart = 0
for key in collatzChainLens.keys():
    if collatzChainLens.get(key) > longestChain:
        longestChain = collatzChainLens.get(key)
        longestStart = key

print(longestStart)
