def fib(n):
    """Print a Fibonacci series up to n."""
    a ,b =0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()


def fib2(n):
    """Print a Fibonaci series upt to n and return it"""
    result = []
    a, b= 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


print("This line will be printed.")

for x in range(1, 10):
    if x == 1:
        # indented four spaces
        print("x is 1.")
    else:
        print("x is ", x, " ")

fib100=fib2(100)
print(fib100)

