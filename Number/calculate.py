def plus(number1=0, number2=0):
    total = number1 + number2
    return total


def fibonacci(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
