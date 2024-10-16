##pow-a-b Вернуть число a в степени b. Используя цикл. Ограничения b > 0 a^b входит в ограничения типа int Sample Input: 2 6 Sample Output: 64
a = 2
b = 4
def pow_a_b(a:int, b:int):
        return a**b
print(f"a**b: {pow_a_b(a, b)}")