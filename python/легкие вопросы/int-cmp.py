## int-cmp
a = 1
b = 8
def int_cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0

print(f"int-cmp: {int_cmp(a, b)}")