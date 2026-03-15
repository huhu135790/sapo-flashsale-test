from queue import PriorityQueue
Q=PriorityQueue()
n,k= map(int,input().split())
for x in input().split(): Q.put(int(x))
res=0
while Q.qsize()>1:
    x=0
    k=min(Q.qsize(),k)
    for i in range (k):x+=Q.get()
    Q.put(x)
    res+=x
print(res)