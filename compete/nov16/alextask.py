
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def bcnn(a, b):
    return a*b / gcd(a, b)

def ms(L):
    kq = bcnn(L[0], L[1])
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if bcnn(L[i], L[j]) < kq :
                kq = bcnn(L[i], L[j])
    return kq

#main
T=int(raw_input())
for t in range(T):
    N = int(raw_input())
    L = []
    L = map(int, raw_input().split())
    print ms(L)
