


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0,n):
        print(a, end='  ')
        c = a + b
        a = b
        b = c



print('Fibonacci series')
n= int(input("Enter the range :"))

fibonacci(n)
