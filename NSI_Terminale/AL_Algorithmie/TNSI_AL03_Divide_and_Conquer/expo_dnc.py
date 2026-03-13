def expo(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return expo(a * a, n // 2)
    return a * expo(a * a, (n-1)//2)

def expo2(a, n):
    for i in range(2, n):
        a = a * a
    return a

