'''
Minh họa
V   10  10  5   14  6
T   6   7   2   3   7

Bước       xét          k           Q            Out
        V     T         0           {}
1       10    6                     {10}          6
2       10    7         6           {10,16}       4+1*7

'''
from queue import PriorityQueue
Q=PriorityQueue()
n=int(input())
V=list(map(int,input().split()))
T=list(map(int,input().split()))
k=0
for v,t in zip(V,T):
    Q.put(v+k)
    s=0
    while Q.qsize() and Q.queue[0]-k <= t: s+=Q.get()-k #tan hết
    print(s+Q.qsize()*t,end=" ")
    k+=t