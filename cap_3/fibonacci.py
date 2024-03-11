import time
import sys
sys.setrecursionlimit(9999)

# O(2^n)
# recursive fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    return value

# memoized O(n)
value_fib = {0:0, 1:1}
def memo_fibonacci(n):
    if n in value_fib:
        
      return value_fib[n]
        
    else:
       
        value_fib[n] = memo_fibonacci(n-1) + memo_fibonacci(n-2)

        return value_fib[n]

# bottom-up
def bottom_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        while n > 0:
            c = b
            b = a + b
            a = c
            n -= 1
        return a

# math
def equation_fibonacci(n):
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return round((phi ** n - psi ** n) / sqrt_5)

start_time = time.time()
# print(fibonacci(35))
print(f'{time.time()-start_time:.3f} seconds elapsed.')

start_time = time.time()
print(memo_fibonacci(10))
print(f'{time.time()-start_time:.3f} seconds elapsed.')

start_time = time.time()
print(bottom_fib(10))
print(f'{time.time()-start_time:.3f} seconds elapsed.')

start_time = time.time()
print(equation_fibonacci(10))
print(f'{time.time()-start_time:.3f} seconds elapsed.')
