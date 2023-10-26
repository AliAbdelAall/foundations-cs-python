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


def inputLimitedList(m):
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
        sub = inputLimitedList(m)
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
        key = input(f"Enter Key {i + 1}: ")
        while key in dct:
            print("Each Key you Enter must be unique")
            key = input(f"Enter Key {i + 1} again: ")
        value = input(f"Enter Value {i + 1}: ")
        dct[key] = value
    return dct


# ###### Function 3 #######

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


# ########### Question_4 ############

# ###### Inputs #######
def intInputMatrix():
    num = input("Enter the number of Employee(s): ")
    while not num.isdigit():
        print("The number of employee(s) must me numeric")
        num = input("Enter the number of Employee(s) again: ")
    return int(num)


def inputMatrixEmployee(n):
    ids = []
    matrix = []
    for i in range(n):
        print()
        print(f"Employee {i + 1}:")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        e_id = input("Enter ID: ")
        while id in ids:
            print("ID is INCORRECT/ALREADY EXIST Enter ID again: ")
        job_title = input("Enter job title: ")
        company = input("Enter company name: ")
        matrix.append([first_name, last_name, e_id, job_title, company])
    return f"\nEmployee(s):\n {matrix}"


# ###### Function 4 #######

def convertMatrixToDictionary(matrix):
    dct = {}
    for i in range(len(matrix)):
        dct[matrix[i][2]] = [matrix[i][0], matrix[i][1], matrix[i][3], matrix[i][4]]
    return dct


# ########### Question_5 ############

# ###### Inputs #######

def inputCheckPalindrome():
    s = input("Enter a word: ")
    while len(s) == 0 or len(s.split()) > 1:
        print("You must enter one Word")
    return s


# ###### Function 5 #######

def checkPalindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


# ########### Question_6 ############

# ###### Inputs #######

def inputList():
    while True:
        try:
            lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
            return lst
        except ValueError:
            print("The list must be numbers!")


def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left_half = mergeSort(lst[:middle])
    right_half = mergeSort(lst[middle:])

    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):

        if left_half[left_index] > right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1

        elif left_half[left_index] < right_half[right_index]:
            merged.append(right_half[right_index])
            right_index += 1

        elif left_half[left_index] == right_half[right_index]:
            merged.append(left_half[left_index])
            merged.append(right_half[right_index])
            left_index += 1
            right_index += 1

    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])

    return merged


def intInputNumber():
    num = input("Enter a number to look for: ")
    while not num.isdigit():
        print("This is not a numeric number!")
        num = input("Enter a number to look for again: ")
    return int(num)


# ###### Function 6 #######

def searchElement(lst, sorted_lst, k):
    print(sorted_lst)
    low = 0
    high = len(sorted_lst) - 1
    while low <= high:
        middle = (low + high) // 2
        if k == sorted_lst[middle]:
            return f"The number {k} was found at index {lst.index(k)}"
        elif k < sorted_lst[middle]:
            high = middle - 1
        elif k > sorted_lst[middle]:
            low = middle + 1
    return f"The number {k} was not found"


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
            print(convertMatrixToDictionary(inputMatrixEmployee(intInputMatrix())))
        elif choice == 5:
            print(checkPalindrome(inputCheckPalindrome()))
        elif choice == 6:
            lst = inputList()
            print(searchElement(lst, mergeSort(lst), intInputNumber()))
        else:
            print("Your choice is INVALID")

        Menu()
        choice = inputChoice()

    print("You EXITED the program...")


main()
