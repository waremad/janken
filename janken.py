import random

def lscount(ls,self):#ある連続する要素の出現回数
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

def clip(ls,self):
    if ls == []:
        return []
    n = how_hand(ls,self)
    ls.append(self)
    if n == 0:
        return ls

    out = []
    sa = len(ls) - n
    for i in range(sa):
        if ls[i:i+n] == ls[-n:]:
#            print(i,n,ls[i:i+n],ls[-n:],ls)
            out.append(ls[i+n])
    return out

def max_pic(ls):
    if ls == []:
        return []
    dic = {}
    for i in ls:
        if i in list(dic.keys()):
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    out = []
    n = max(list(dic.values()))
    for i in list(dic.keys()):
        if dic[i] == n:
            out.append(i)
    return out

def janwin(ls):
    if ls == []:
        return random.choice(["g","c","p"])
    if len(ls) == 3:
        return random.choice(["g","c","p"])
    if len(ls) == 1:
        return win(ls[0])
    if win(ls[0]) == ls[1]:
        return ls[1]
    else:
        return ls[0]

def jprint(me,cp,log):

    print("total game :",len(log))
    if len(log) == 0:
        pass
    else:
        cpwin = 0
        cpdraw = 0
        mewin = 0
        for i in log:
            if i == "cp":
                cpwin += 1
            elif i == "draw":
                cpdraw += 1
            else:
                mewin += 1
        print("cp total win :" ,cpwin)
        print("total draw :" ,cpdraw)
        print("me total  win :" ,mewin)
        print("cp win% :" , round((cpwin*100)/len(log)))
        print("draw% :" ,round((cpdraw*100)/len(log)))
        print("me win% :" ,round((mewin*100)/len(log)))

        if len(log) > 10:
            cpwin = 0
            cpdraw = 0
            mewin = 0
            for i in log[-10:]:
                if i == "cp":
                    cpwin += 1
                elif i == "draw":
                    cpdraw += 1
                else:
                    mewin += 1
            print("cp last10 win :" ,cpwin)
            print("last10 draw :" ,cpdraw)
            print("me last10 win :" ,mewin)
    print(log)
    if log[-1] == "draw":
        result = "draw"
    else:
        result = log[-1] + " win"
    print("\n" + "CP:" + cp)
    print(result)
    print("you:" + me + "\n")

def judge(me,cp):
    if me == cp:
        return "draw"
    if win(cp) == me:
        return "me"
    else:
        return "cp"

"""
g 4
c 3
p 3
g w3 d4 l3
c w3 d3 l4
p w4 d3 l3
"""

gcp = ["g","c","p"]
cphand = random.choice(gcp)
mehand = ""
while not(mehand in gcp):
    mehand = input("your hand " + cphand)
handlog = [mehand]
winlog = [judge(mehand,cphand)]
jprint(mehand,cphand,winlog)
n = 30
while not(winlog.count("me") == n or winlog.count("cp") == 30):
    cphand = janwin(max_pic(clip(handlog,mehand)))
    mehand = ""
    while not(mehand in gcp):
        mehand = input("your hand "+ cphand)
    handlog.append(mehand)
    winlog.append(judge(mehand,cphand))
    jprint(mehand,cphand,winlog)