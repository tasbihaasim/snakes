def base_2_converter(n):
    m=[]
    u=''
    while n!=0:
        x=int(n%2)
        n=n//2
        m.append(x)
        for k in range(len(m)):
            c=str(m.pop())
            u=u+c
    return int(u)

def push(lst, item):
    lst.append(item)
