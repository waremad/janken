import random

def lscount(ls,self):
    if len(ls) < len(self) or ls == [] or self == []:
        return 0
    sa = len(ls) - len(self) + 1
    out = 0
    for i in range(sa):
        if ls[i:i+len(self)] == self:
            out = out + 1
    return out


def how_hand(ls,self):#何手ごとの統計を取ればよいか
    n = len(ls)-1
    count = 0
    conti = True
    while conti:
        lis = ls[-n:]
        lis.append(self)
        if lscount(ls,lis) >= 2:
            return n+1
        elif n == 0:
            if self in ls:
                return 1
            else:
                return 0
        n = n - 1

def win(self):
    dic = {"g":"p","c":"g","p":"c"}
    return dic[self]