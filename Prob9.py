def findPythagTriplet():
    for x in range(1, 999):
        for y in range(x, 999):
            z = 1000 - y - x
            if z < y:
                continue
            if x ** 2 + y ** 2 == z ** 2:
                return x * y * z  # Due to the need to break out of a nested loop the advised strategy is a return


print(findPythagTriplet())
