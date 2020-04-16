import math
def length_of_line(points_lists, length):
    y=[]
    for i in points lists:
        a=i[1][0]
        b=i[0][0]
        c=i[1][1]
        d=i[0][1]
        x=math.sqrt(((a-b)*(a-b))+((c-d)*(c-d)))
        y.append(x)
    return binary_search_iterative(y, length)


def binary_search_iterative(lst, item):
    top=len(lst)-1
    bottom=0
    mid=(top+bottom)//2
    u=None
    while bottom<=top:
        a=round(float((lst[mid])), 2)
        if item == a:
            u=mid
            return u
        elif item > a:
            bottom=mid+1
            mid=(top+bottom)//2
        elif item < a:
            top=mid-1
            mid=(top+bottom)//2
    if u==None:
        return -1
