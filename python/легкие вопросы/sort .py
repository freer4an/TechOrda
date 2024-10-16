arr = [7, 3, 5, 8, 1, 3, 2]
def sort_arr(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

print(f"sort: {sort_arr(arr)}")