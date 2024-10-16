def is_prime(n: int) -> bool:
    for i in range(2, n//2+1):
        if n % i == 0:
            return "not prime"
    return "prime"

n = int(input("number = "))
print(f"{n} is {is_prime(n)}")
