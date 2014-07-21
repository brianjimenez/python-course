#cython: boundscheck=False
#cython: wraparound=False

def fib(long n):
    """Print the Fibonacci series up to n."""
    cdef long a = 0
    cdef long b = 1
    while b < n:
        print b,
        a, b = b, a + b
