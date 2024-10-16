def odd_even(n: int):
    return n % 2 == 0


n = int(input("n = "))
if odd_even(n):
    print(f"{n} is EVEN")
else:
    print(f"{n} is ODD")