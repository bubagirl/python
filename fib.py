def fibonacci(n):
    num = range(0, n)
    fib = lambda x: x if x <= 2 else fib(x-1) + fib(x-2)
    f = list(map(fib, num))
    res = list(filter(lambda i: i % 2 == 0, f))
    print(res)
fibonacci(10)
