def test(x,n):
    if n <= 1:
        return 0
    if x % n == 0:
        return 1 + test(x,n - 1)
    else:
        return test(x,n - 1)

print(test(67,3))