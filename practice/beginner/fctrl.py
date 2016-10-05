"""
def factorial(n):
    f = 1
    for i in range(1,n + 1):
        f *= i
    return f
"""

def Z(n):
    """
    20 = 5 * 2 * 2
    25 = 5^2 
    50 = 5^2 * 2
    """
    count5 = 0
    i = 1
    while 1:
        a = pow(5, i)
        if a > n:
            return count5
        else:
            count5 += n/a
            i += 1

def main():
    T = int(raw_input())
    for t in range(T):
        N = int(raw_input())
        print Z(N)

main()
