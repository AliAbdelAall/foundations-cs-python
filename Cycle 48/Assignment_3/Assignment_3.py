# ########### User Login ############

def userLogin():
    print("login")
    username = input("Enter yor username: ")
    return f"Welcome, {username}"


# ########### Question_1 ############

# ###### Input #######:

def lenInput():
    num = input("Enter the length of the Matrix: ")
    while not num.isdigit():
        print("The length must me numeric")
        num = input("Enter the length of the Matrix again: ")
    return num


def sublistLenInput():
    num = input("Enter the length of the Sub-lists: ")
    while not num.isdigit():
        print("The length must me numeric")
        num = input("Enter the length of the Sub-lists again: ")
    return num


def inputList(m):
    while True:
        try:
            lst = list(map(int, input(f"Enter a list of {m} numbers separated by spaces: ").split()))
            if len(lst) != m:
                print(f"You must input {m} numbers")
            else:
                return lst
        except ValueError:
            print("The list must be all numbers")


def inputMatrix(n, m):
    matrix = []
    for i in range(n):
        sub = inputList(m)
        matrix.append(sub)
    return matrix


def addMatrices(matrix_1, matrix_2):
    res = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[i])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        res.append(row)
    return res
