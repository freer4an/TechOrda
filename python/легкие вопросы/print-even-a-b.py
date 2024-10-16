##print-even-a-b
a = 1
b = 10
def print_even_a_b(a:int, b:int):
    return [i for i in range(a, b+1) if i % 2 == 0]

print(f"print-even-a-b: {print_even_a_b(a, b)}")