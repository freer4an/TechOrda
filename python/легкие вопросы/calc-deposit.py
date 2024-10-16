##calc-deposit
n = 2
k = 5
b = 1000
def calc_deposit(n, k, b):
    return b * (1 + k / 100) ** n

print(f"calc-deposit: {calc_deposit(n, k ,b):.2f}")