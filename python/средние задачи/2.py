def is_palindrome(s: str):
    return s == s[::-1]

s = str(input("s = "))
if is_palindrome(s):
    print(f"{s} is palindrome")
else:
    print(f"{s} is NOT palindrome")