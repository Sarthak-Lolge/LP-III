# pr1


# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Non-Recursive (Iterative) Fibonacci
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Input and Output
n = int(input("Enter value of n: "))

print("Fibonacci using Recursive method:", fib_recursive(n))
print("Fibonacci using Iterative method:", fib_iterative(n))