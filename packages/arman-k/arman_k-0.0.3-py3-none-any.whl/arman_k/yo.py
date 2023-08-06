def binary_to_decimal(a):
    s,j = 0,0
    while a > 0 :
        r = a % 10
        s += r * (2**j)
        a //= 10
        j += 1
    print(s)

def fibonacci(a):
    n1 = 0
    n2 = 1
    for fib in range(0,a):
        print(n1,end=",")
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    print()