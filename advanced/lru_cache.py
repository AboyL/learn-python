from functools import  lru_cache
@lru_cache()
def fib2(n):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

print(fib2(40))