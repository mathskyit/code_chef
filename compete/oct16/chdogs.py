import math

def dogs():
    return

def main():
    T = int(raw_input())
    for t in range(T):
        s, v = map(float, raw_input().split())
        print "%0.2f" % (2*math.pi*s/(math.sqrt(3)*v*6))
main()
