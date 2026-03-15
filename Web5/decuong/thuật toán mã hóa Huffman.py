from collections import Counter
from queue import PriorityQueue
Q=PriorityQueue()
F=Counter(input())
for x in F.values(): Q.put(int(x))
res=0
while Q.qsize()>1:
    x = Q.get() + Q.get()
    Q.put(x)
    res += x
print(res)