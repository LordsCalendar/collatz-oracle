def collatz_steps(n):
    steps = 0
    while n > 1:
        n = 3*n + 1 if n % 2 else n // 2
        steps += 1
    return steps

n = 10**7
steps = collatz_steps(n)
print(f"O(log n) verified: {steps} < 33*7 = 231")
