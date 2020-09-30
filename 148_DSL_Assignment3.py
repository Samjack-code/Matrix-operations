def accept(L,r,c):
    for i in range(r):
        L1 = []
        for j in range(c):
            L1.append(int(input()))#ere inbuilt functions are not used.
            #for better logic understanding 
        L.append(L1)
        
def show(L,r,c):
    for i in range(r):
        for j in range(c):
            print(L[i][j],end="   ")
        print()

def Addition(A,B,C,r1,c1):
    for i in range(r1):
        for j in range(c1):
            C[i][j] = A[i][j] + B[i][j]
    print("Addition of the matrix is :")
    show(C,r1,c1)
    
def Subtraction(A,B,C,r1,c1):
    for i in range(r1):
        for j in range(c1):
            C[i][j] = A[i][j] - B[i][j]
    print("Subtraction of the matrix is :")
    show(C,r1,c1)

def Multiplication(A,B,C,r1,c1,c2):
    for i in range(r1):
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum = sum + (A[i][k] * B[k][j])
            C[i][j] = sum
    print("Matrix multiplication is :")
    show(C,r1,c2)

def Transpose(T,M,r,c):
    for i in range(r):
        for j in range(c):
            T[i][j] = M[j][i]
    show(T,r,c)
    
while True:
    print("1. Accept the matrix ")
    print("2. Display the matrix ")
    print("3. Addition of the matrix ")
    print("4. Subtraction of the matrix ")
    print("5. Multiplication of the matrix ")
    print("6. Transpose of the matrix ")
    print("0.  Exit the program!!!")
    ch = int(input("Enter your choice : "))
    C = []
    if(ch == 0):
        print("Program terminated!!!")
        break
    elif(ch == 1):
        A = []
        B = []
        print("Enter first matrix ")
        r1 = int(input("Enter number of rows : "))
        c1 = int(input("Enter number of columns : "))
        accept(A,r1,c1)
        print("Enter second matrix ")
        r2 = int(input("Enter number of rows : "))
        c2 = int(input("Enter number of columns : "))
        accept(B,r2,c2)
    elif(ch == 2):
        print("First matrix : ")
        show(A,r1,c1)
        print("Second matrix : ")
        show(B,r2,c2)
    elif(ch == 3):
        if(r1==r2 and c1==c2):
             C = [[0 for j in range(c1)]for i in range(r1)]
             Addition(A,B,C,r1,c1)
        else:
            print("Addition of the matrix not possible!!!")
    elif(ch == 4):
        if(r1==r2 and c1==c2):
             C = [[0 for j in range(c1)]for i in range(r1)]
             Subtraction(A,B,C,r1,c1)
        else:
            print("Subtraction of the matrix not possible!!!")
    elif(ch == 5):
        if(c1 == r2):
            C = [[0 for j in range(c2)]for i in range(r1)]
            Multiplication(A,B,C,r1,c1,c2)
        else:
            print("Matrix multiplication not possible!!!")
    elif(ch == 6):
        print("Transpose of matrix A is :")
        T = [[0 for j in range(r1)]for i in range(c1)]
        Transpose(T,A,r1,c1)
        print("Transpose of matrix B is :")
        T = [[0 for j in range(r2)]for i in range(c2)]
        Transpose(T, B, r2, c2)
    else:
        print("Invalid option!!! please enter valid ")
