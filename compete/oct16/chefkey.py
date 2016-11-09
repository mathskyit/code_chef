import math

def chefkey(a, b, c):
    count = 0
    for i in range(1, a+1):
        x = float(c)/i
        if math.floor(x) == x and x > 0 and x <= b:
            count +=1
    return count

def main():
    T = int(raw_input())
    for t in range(T):
        a, b, c = map(int, raw_input().split())
        print chefkey(a, b, c)
main()
