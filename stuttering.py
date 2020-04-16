def deQueue(lst):
    x=lst.pop()
    return x

def enQueue(lst,data):
    y=[data]
    y=y+lst
    return y


def stut(lst):
    a=[]
    p=deQueue(lst)
    a.append(p)
    a=enQueue(a,p)
    return a

def stutter(lst):
    t=[]
    for i in range(len(lst)):
        w=stut([lst[i]])
        t=t+w
    return t
