def binary_search_iterative_modified(lst, item):
    top=len(lst)-1
    bottom=0
    mid=(top+bottom)//2
    u=None
    while bottom<=top:
        if item==lst[mid]:
            u=mid
            return u
        if mid<bottom:
            return 0
        elif item>lst[mid]:
            bottom=mid+1
            mid=(top+bottom)//2
        elif item<lst[mid]:
            top=mid-1
            mid=(top+bottom)//2
    if u==None:
        return bottom
