def productFib(prod):
    # your code
    fib_sequence = [0, 1]

    while True:
        if (fib_sequence[-2] * fib_sequence[-1]) == prod:
            return [fib_sequence[-2], fib_sequence[-1], True]
        elif (fib_sequence[-2] * fib_sequence[-1]) > prod:
            return [fib_sequence[-2], fib_sequence[-1], False]
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            
print(productFib(4895))
print(productFib(5895))
print(productFib(0))