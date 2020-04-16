def matrix_multiplication(A,B):
    if len(A[0])==len(B):
        zero =[]
        for i in range(len(A)):
            lst = []
            for j in range(len(B[0])):
                sum = 0
                for k in range(len(B)):
                    sum += A[i][k]*B[k][j]
                lst.append(sum)
            zero.append(lst)
        return zero
    else:
        return "Multiplication not possible"
