# ########### User Login ############

def userLogin():
    print("login")
    username = input("Enter yor username: ")
    return f"Welcome, {username}"


# ########### Question_1 ############

# ###### Input #######

def lenInput():
    num = input("Enter the length of the Matrix: ")
    while not num.isdigit():
        print("The length must me numeric")
        num = input("Enter the length of the Matrix again: ")
    return int(num)


def sublistLenInput():
    num = input("Enter the length of the Sub-lists: ")
    while not num.isdigit():
        print("The length must me numeric")
        num = input("Enter the length of the Sub-lists again: ")
    return int(num)


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


# ###### Function 1 #######

def addMatrices(matrix_len, sub_len):  #
    matrix_1 = inputMatrix(matrix_len, sub_len)
    matrix_2 = inputMatrix(matrix_len, sub_len)
    res = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[i])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        res.append(row)
    return res


# ########### Menu ############

def Menu():
    print("""
    1. Add Matrices
    2. Check Rotation
    3. Invert Dictionary
    4. Convert Matrix to Dictionary
    5. Check Palindrome
    6. Search for an Element & Merge Sort
    7. Exit""")


# ########### Choice ############

def inputChoice():
    choice = input("Enter you choice: ")
    while not choice.isdigit():
        print("Your choice must be numeric.")
        choice = input("Enter you choice again: ")
    return choice


