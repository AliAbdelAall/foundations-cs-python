# ########### User Login ############

def userLogin():
    print("login")
    username = input("Enter yor username: ")
    return f"Welcome, {username}"


# ########### Question_1 ############

def addMatrices(matrix_1, matrix_2):
    res = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1(i))):
            row.append(matrix_1[i][j]+matrix_2[i][j])
        res.append(row)
    return res
