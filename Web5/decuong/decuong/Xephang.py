'''
ý tươngr:
Dùng stack chứa các phần tử (gia trị, tần suất)
4 7 2 8 4 4 4 6
Bước             xét          Stack                           res
                              []                              0
1                4            [(4,1)]                         0
2                7            [(7,1)]                         1
3                2            [(7,1)(2,1)]                    1
4                6            [(7,1)(6,1)]                    1+1
5                4            [(7,1)(6,1)(4,1)]               1
6                6            [(7,1)(6,2)]                    1+1+1
7                4            [(7,1)(6,2)(4,1)]               1
8                6            [(7,1)(6,3)]                    1+2+1


Thuat toan:
B1: Nhap n vao dãy a
B2: Khai báo Stack S
B3: res=0
B4: Duyệt x trên a
    + Lấy hết cấc phần tử nhỏ hơn x khỏi S cộng tuần xuất vào res
    + Nếu top =x thì cộng tần suất vào res và kiểm tra nêú S.qsize()==2 thì res++
            Sau đó tần suất top lên 1
    + Ngược lại thì S.qsize() >= 1 thì res++ say đó đưa (x,1) Vào S
B5: Xuất res
'''
#xếp hàng
from queue import LifoQueue
n=int(input())
S=LifoQueue()
res=0
for x in map(int,input().split()):
    while S.qsize()>0 and S.queue[-1][0]<x: res+=S.get()[1]
    if S.qsize()>0 and S.queue[-1][0]==x:
        res+=S.queue[-1][1]+ (S.qsize()>=2)
        S.queue[-1][1]+=1
    else:
        res+=(S.qsize()>=1)
        S.put([x,1])
print(res)