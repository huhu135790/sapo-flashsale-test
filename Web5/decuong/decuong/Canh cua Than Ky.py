'''
Canh Cua Thần Kỳ
Tìm người trong dãy A B C D E A A B B C C D D  E E A A A A ...

bước                n                   Queue
                    100                 [(A,1) (B,1) (C,1) (D,1) (E,1)]
1                   99                  [(B,1) (C,1) (D,1) (E,1) (A,2)]
2                   98                  [(C,1) (D,1) (E,1) (A,2) (B,2)]
3
4
5                   95                  [(A,2) (B,2) (C,2) (D,2) (E,2)]
6                   93                  [(B,2) (C,2) (D,2) (E,2) (A,4)]
7                   91
8                   89
9                   87
10                  85                  [(A,4) (B,4) (C,4) (D,4) (E,4)]
11                  81
12                  77
13                  73
14                  69
15                  65                  [(A,8) (B,8) (C,8) (D,8) (E,8)]
16                  57
17                  49
18                  41
19                  33
20                  25                  [(A,16) (B,16) (C,16) (D,16) (E,16)]
21                  9                   [(B,16) (C,16) (D,16) (E,16) (A,32)]

Xuat B vì n còn 9 mà B có 16 chữ

Thuat Toán
B1: Khai báo Queue Q
B2: Đưa A,B,C,D,E với tần suất 1 vào Q
B3: Nhap n
B4: Nếu n lớn hơn tần suất phần tử dâù thì n giảm đi tần suất đó, lấy ptu dầu
nhân tần suất lên với 2 và thêm vào cuối
B5: Lập lại bước 4 tới khi n<= tần suất ptu đứng đầu thì xuất tên ng
dùng đúng đầy
'''

from queue import Queue
def sol():
    Q = Queue()
    for x in "dangdungcntt","tienquanutc","quang123","maianh","nguyenminhduc2820":
        Q.put((x,1))
    n= int(input())
    while n>Q.queue[0][1]:
        t,f=Q.get()
        n-=f
        Q.put((t,2*f))
    print(Q.get()[0])
for i in range (int(input())):sol()