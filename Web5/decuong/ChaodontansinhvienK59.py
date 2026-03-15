#Chào đón k59
'''
Thuat toan:
B1: Nhập n và dãy a
B2: Khai báo Stack S
B3: Đưa (inf,-1) vào S
B4:Duyệt I từ 0 đến n-1
    +Lấy hết những số nhỏ hơn học bằng  a(i)
    +l[i]=S.top.vitri
    +Đưa a([i],i) vào S
B5:Tương tự duyệt từ phải sang  xây dựng mảng R tìm vị trí những phần tử cao hơn
    gần nhất bên phải
B6: Duyêt I=0 đến n-1
    Li và Ri nếu có phần tử là -1 lấy phần tử còn lại
    Ngược lại  so sánh i-Li và Ri-I bên nào nhỏ hơn thì lấy ( ưu tiên bên trái)
    '''


from queue import LifoQueue

def fun(a,id):
    S=LifoQueue()
    S.put((2e9,-1))
    L=[0]*len(a)
    for i,x in zip(id,a):
        while S.queue[-1][0]<=x: S.get()
        L[i]=S.queue[-1][1]
        S.put((x,i))
    return L
if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    L=fun(a,range(n))
    R=fun(a[::-1],range(n-1,-1,-1))
    for i in range(n):
        if L[i]==-1 or R[i]==-1: print(L[i]+R[i]+1,end=" ")
        else: print(L[i] if i-L[i]<=R[i]-i else R[i],end=" ")