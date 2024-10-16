##sum
arr = [1,2,3,5,6]
def arr_sum(arr: list[int]):
    res = 0
    for el in arr:
        res += el
    return res

print(f"sum: {arr_sum(arr)}")