##sqr-sum-1-n
n=8
def sqr_sum_1_n(n:int):
    if n < 1 or n > 10860:
        return 0
    sum=0
    for i in range(1, n+1):
        sum += i*i
    return sum

print(f"sqr-sum-1-n: {sqr_sum_1_n(n)}")