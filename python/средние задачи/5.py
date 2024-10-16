def is_perfect(n: int):
    sm = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sm += i

    return n == sm

start = 1
end = 1000
result = [i for i in range(start, end+1) if is_perfect(i)]
print(result)
