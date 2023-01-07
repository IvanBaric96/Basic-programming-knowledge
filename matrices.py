import random
from re import L

def create_list(length, r=15):
    l=[0]*length
    for i in range(0, length):
        l[i]=random.randint(0,r)
    return l
#print(create_list(10))


def create_matrix(n_rows,n_col, r=15):
    mat=[0]*n_rows
    for i in range(n_rows):
        mat[i]=create_list(n_col,r)
    return mat
#print(create_matrix(3,4))


def add_matrices(mat1, mat2):
    if len(mat1)!=len(mat2) or len(mat1[1])!=len(mat2[1]):
        return("Matrices must have equal number of rows and columns!")
    mat=mat1
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
             mat[i][j]=mat1[i][j]+mat2[i][j]
    return mat
# mat1=create_matrix(3,4)
# mat2=create_matrix(3,4)
# print(mat1)
# print(mat2)
# print(add_matrices(mat1,mat2))


def multiply_lists(l1, l2):
    if len(l1)!=len(l2):
        return("Lists must be of equal length!")
    res=0
    for i in range(len(l1)):
        res+=l1[i]*l2[i]
    return res
# l1=create_list(5,4)
# l2=create_list(5,4)
# print(l1)
# print(l2)
# print(multiply_lists(l1, l2))

def i_th_col(mat,i):
    res=[0]*len(mat)
    for j in range(0, len(mat)):
        res[j]=mat[j][i]
    return res
# mat=create_matrix(4,5)
# print(mat)
# print(i_th_col(mat,3))


def multiply_matrices(mat1, mat2):
    if len(mat1[1])!=len(mat2):
        return("Number of columns of matrix1 must be equal to number of rows of matrix2!")
    res=[[0]*len(mat2[1])]*len(mat1)
    for i in range(0,len(mat1)):
        for k in range(0, len(mat2[1])):
            print("i: "+str(i)+" k: "+str(k))
            print(mat1[i])
            print(i_th_col(mat2,k))
            i_k=multiply_lists(mat1[i], i_th_col(mat2,k))
            print(i_k)
            res[i][k]=i_k
            print("-----")  
        print("-----------------------------")
    return res  
# mat1=create_matrix(3,4,5)
# mat2=create_matrix(4,5,5)
# print(mat1)
# print(mat2)
# print(multiply_matrices(mat1, mat2))


def average_of_list(l):
    r=0
    for i in range(0, len(l)):
        r+=l[i]
    return r/len(l)
# l=create_list(5,5)
# print(l)
# print(average_of_list(l))


def average_by_rows(mat):
    res=[0]*len(mat)
    for i in range(len(mat)):
        res[i]=average_of_list(mat[i])
    return res
# m=create_matrix(3,4,5)
# print(m)
# print(average_by_rows(m))


def average_by_cols(mat):
    res=[0]*len(mat[1])
    for i in range(0, len(mat[1])):
        res[i]=average_of_list(i_th_col(mat,i))
    return res
# m=create_matrix(3,4,5)
# print(m)
# print(average_by_cols(m))

def transpose_matrix(mat):
    mat_tr=create_matrix(len(mat[1]), len(mat))
    for i in range(0, len(mat[1])):
        for j in range(0, len(mat)):
            mat_tr[i][j]=mat[j][i]
    return mat_tr
m=create_matrix(3,4)
print(m)
print(transpose_matrix(m))
