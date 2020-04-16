def deQueue(lst):
    x=lst.pop()
    return x

def enQueue(lst,data):
    y=[data]
    y=y+lst
    return y

def mirror(lst):
    a=[]
    t=[]
    for i in range(len(lst)):
        p=deQueue(lst)
        a.append(p)
        a=enQueue(a,p)
    return a
