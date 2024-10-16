def is_perfect(n: int):
    sm = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sm += i

    return n == sm

n = int(input("n = "))
if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")