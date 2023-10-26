# ########### User Login ############

def userLogin():
    print("login")
    username = input("Enter yor username: ")
    print(f"Welcome, {username}")


# ########### Question_1 ############

# ###### Inputs #######

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
            print("The list must be all numbers\n")


def inputMatrix(n, m):
    matrix = []
    for i in range(n):
        sub = inputList(m)
        matrix.append(sub)
    return matrix


# ###### Function 1 #######

def addMatrices(matrix_len, sub_len):
    print()
    print("For the first Matrix:")
    matrix_1 = inputMatrix(matrix_len, sub_len)
    print()
    print("For the second Matrix:")
    matrix_2 = inputMatrix(matrix_len, sub_len)
    print()
    res = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[i])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        res.append(row)
    return f"the addition of both matrices is {res}"


# ########### Question_3 ############

# ###### Inputs #######
def inputDictItemsNumber():
    num = input("Enter the number of items: ")
    while not num.isdigit():
        print("Number of items must be numeric")
        num = input("Enter the number of items again: ")
    return int(num)


def inputDict(n):
    dct = {}
    for i in range(n):
        key = input(f"Enter Key {i+1}: ")
        while key in dct:
            print("Each Key you Enter must be unique")
            key = input(f"Enter Key {i + 1} again: ")
        value = input(f"Enter Value {i+1}: ")
        dct[key] = value
    return dct


def invertDictionary(dct):
    inv_dict = {}
    for key, value in dct.items():
        if value in inv_dict:
            if type(inv_dict[value]) == list:
                inv_dict[value].append(key)
            else:
                inv_dict[value] = [inv_dict[value], key]
        else:
            inv_dict[value] = key
    return f"Your dictionary: {dct}\nInverted dictionary: {inv_dict}"


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
    return int(choice)


def main():
    userLogin()
    Menu()
    choice = inputChoice()
    print()

    while choice != 7:
        if choice == 1:
            print(addMatrices(lenInput(), sublistLenInput()))
        elif choice == 2:
            pass
        elif choice == 3:
            print(invertDictionary(inputDict(inputDictItemsNumber())))
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        else:
            print("Your choice is INVALID")

        Menu()
        choice = inputChoice()

    print("You EXITED the program...")


main()
