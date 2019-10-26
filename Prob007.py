primes = [2]
s = 3
while len(primes) < 10001:
    if all([s%x for x in primes]):
        # modulo operator gives 0 for even divisibility which evaluates as false and fails the if-all check
        primes.append(s)
    s += 1

print(primes[10000])
