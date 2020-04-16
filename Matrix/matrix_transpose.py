def matrix_transpose(A):
    res=[]
    for i in range(len(A[0])):
        t=[]
        for j in range(len(A)):
            t.append(A[j][i])
        res.append(t)
    return res
