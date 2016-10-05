def factorial(n):
    f = 1
    for i in range(1,n + 1):
        f *= i
    return f


def main():
    T = int(raw_input())
    for t in range(T):
        N = int(raw_input())
        print factorial(N)

main()
