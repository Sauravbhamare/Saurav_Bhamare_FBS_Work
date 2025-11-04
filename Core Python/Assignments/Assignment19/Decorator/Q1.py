def memoize(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]
        result = func(x)
        cache[x] = result
        return result

    return wrapper

@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(6))

