import numpy as np

def readMatrix(x,r,c):
    for i in range(r):
        for j in range(c):
            x[i][j]=int(input(f'Enter elements at position {i+1},{j+1}: '))

r1 = int(input('Rows of A\n'))
r2 = int(input('Rows of B\n'))
c1 = int(input('Columns of A\n'))
c2 = int(input('Columns of B\n'))

print('Enter Matrix A:\n')
A = np.zeros((r1,c1),dtype=int)
readMatrix(A,r1,c1)

print('Enter Matrix B:\n')
B = np.zeros((r2,c2),dtype=int)
readMatrix(B,r2,c2)

if r1!=r2 or c1!=c2:
    print('Matrix Addition not possible')
else:
    print('Matrix A:\n')
    print(A)

    print('Matrix B:\n')
    print(B)

    C= A+B
    print('Addition: \n')
    print(C)

    print('Transpose: \n')
    print(C.T)