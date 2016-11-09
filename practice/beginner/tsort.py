# all sort algorithms

def insertion(L):
    for i in range(1, len(L)):
        x = L[i]
        j = i - 1
        while j >= 0 and L[j] > x:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = x
    return L

def selection(L):
    for i in range(0,len(L)-1):
        iMin = i
        for j in range(i+1, len(L)):
            if L[j] < L[iMin]:
                iMin = j
        L[i], L[iMin] = L[iMin], L[i]
    return L

def print_perline(L):
    for i in L:
        print i

def main():
    # len
    N = int(raw_input())
    L = []
    for i in range(N):
        L.append(int(raw_input()))
    ###
    L2 = insertion(L)
    #L2 = selection(L)
    #print_perline(L2)
    print L2

main()
