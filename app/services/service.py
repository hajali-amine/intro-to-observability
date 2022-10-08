def factorial(n: int) -> int:
    if n < 0:
        return Exception("n can't be negative")
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod