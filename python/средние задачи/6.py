def fibonacci_seq(n: int):
    i = 0
    seq = [0,1]
    while i < n:
        seq.append(seq[-1] + seq[-2])
        i=seq[-1]
    return seq

n = int(input("n = "))
if n in fibonacci_seq(n):
    print(f"{n} is IN fibonacci sequence")
else:
    print(f"{n} is NOT in fibonacci sequence")