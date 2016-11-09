#main
T = int(raw_input())
for t in range(T):
    K = int(raw_input())
    #process
    for i in range(K):
        for j in range(K-1, -1, -1): print ((j+i)%K)+1,
        print '\n'
