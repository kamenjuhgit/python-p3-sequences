#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    j = 0
    for j in range(length):
        if j == 0:
            fibonacci.append(0)
        elif j == 1:
            fibonacci.append(1)
        else:
            k = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(k)
    
    print(fibonacci)

print_fibonacci(10)