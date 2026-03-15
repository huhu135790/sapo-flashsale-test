'''
Vd:khối lượng hóa chất
CH3((CHCO2H)2(CH2)8CO2H)3H2CO3H
Thuat Toan
B1: Khai bao Stack
b2: Nhap công thức x
b3: Nhap c tren x
    Nếu c là C,H,O,( đưa tương ứng 12, 1,16,0 vao S
    Nếu c là ) cộng dồn các số khác 0 lấy từ S thay cho số 0 đầu tiên
    Nếu c là số thì nhân top theo số đó
b4: Cộng dồn S ra kết quả


Cach1:
while S.queue[-1] != 0:
                t+=S.get()
            S.get()
            S.put(t)
        elif c.isdigit():
            so=int(c)
            x=S.get()
            S.put(x*so)
    kq = 0
    for v in S.queue:
        kq+=v
    print(kq)
'''
D={'C':12,'H':1,'O':16,'(':0}
from queue import LifoQueue
def sol():
    S=LifoQueue()
    for c in input():
        if c in D.keys():S.put(D[c])
        elif c==')':
            t=0;
            while S.queue[-1] != 0:t+=S.get()
            S.queue[-1]=t   #S.get()
                            #S.put(t)
        else: S.queue[-1]*=int(c)
    print(sum(S.queue))
if __name__=='__main__':
    for i in range(int(input())):sol()

