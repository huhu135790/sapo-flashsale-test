'''
Tìm đường đi ngắn nhất trong mê cung
đi từ tọa độ (7,3) đến (23,7)
Bước        xét         Next        Queue
                                    [7,3]
1           (7,3)       (8,3)(6,3)  [(8,3)(6,3)]
2           (8,3)       (9,3)       [(6,3) (9,3)]
......

Thuật toán
B1: Nhập n,m
B2: nhâpj ma trận a(n*m)
B3: Xây dựng rào bao xung quanh ma trận toàn 1
B4: Khai báo Q
B5: Nhạp sx,sy,va,fy,fx
B6: Đưa (sx,sy) vào Q và đồng thời a[sx][sy]=1
B7: lấy (u,v) ra khỏi Q và xét 4 láng giềng xem có số 0 thì đưa vào Q
đồng thời đánh số trên ma trạn là a[u][v]+1
B8: lập lại B7 tới khi Q rỗng hoặc a[fx][fy]!=0 thì đừng xuất a[fx][fy]-1
'''

from queue import Queue
n,m=map(int,input().split())
A=[[1]*(m+2)] #rao hang 1
for i in range(n):
    a=list(map(int,input().split()))
    A.append([1]+a+[1])
A.append([1]*(m+2))
sx,sy,fx,fy=map(int,input().split())
Q=Queue()
Q.put((sx,sy))
A[sx][sy]=1
while Q.qsize()>0 and A[fx][fy]==0:
    u,v=Q.get()
    for i,j in (-1,0), (1,0), (0,-1), (0,1):
        if A[u+i][v+j]==0:
            A[u+i][v+j]=A[u][v]+1
            Q.put((u+i,v+j))
print(A[fx][fy]-1)