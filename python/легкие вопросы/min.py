##Min
arr = [5,2,1,4,3]
def min_arr(arr: list[int]):
    if len(arr) == 0:
        return 0
    
    res = arr[0]
    for i in range(1, len(arr)):
        if res > arr[i]:
            res = arr[i]
            
    return res

print(f"min: {min_arr(arr)}")