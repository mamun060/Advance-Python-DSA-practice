# Fibonacci series using recursion 
def Fibonacci(n):
    if n  <= 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(8))