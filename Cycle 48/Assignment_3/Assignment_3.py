# ########### User Login ############

def userLogin():  # O(1), since it does only print and take input
    print("login")
    username = input("Enter yor username: ")
    print(f"Welcome, {username}")


# ########### Question_1 ############

# ###### Inputs #######

def lenInput():  # O(N) N being the number of wrong inputs by the user
    num = input("Enter the length of the Matrix: ")
    while len(num.split()) > 1 or not num.isdigit():
        if len(num.split()) > 1:
            print("You must enter one number")
        elif not num.isdigit():
            print("The length must me numeric")
        num = input("Enter the length of the Matrix again: ")
    return int(num)


def sublistLenInput():  # O(N) N being the number of wrong inputs by the user
    num = input("Enter the length of the Sub-lists: ")
    while len(num.split()) > 1 or not num.isdigit():
        if len(num.split()) > 1:
            print("You must enter one number")
        elif not num.isdigit():
            print("The length must me numeric")
        num = input("Enter the length of the Sub-lists again: ")
    return int(num)


def inputLimitedList(m):  # O(N) N being the number of wrong inputs by the user
    while True:
        try:
            lst = list(map(int, input(f"Enter a list of {m} numbers separated by spaces: ").split()))
            if len(lst) != m:
                print(f"You must input {m} numbers")
            else:
                return lst
        except ValueError:
            print("The list must be all numbers\n")


def inputMatrix(n, m):  # O(N) N the length of the list
    matrix = []
    for i in range(n):
        print(f"{n - i} sub-list(s) left.")
        sub = inputLimitedList(m)
        matrix.append(sub)
    return matrix


# ###### Function 1 #######

def addMatrices(matrix_len, sub_len):  # O(N^2) or O(n*m) n:matrix_len , m:sub_len
    print("\nFor the first Matrix:")
    matrix_1 = inputMatrix(matrix_len, sub_len)
    print("\nFor the second Matrix:")
    matrix_2 = inputMatrix(matrix_len, sub_len)
    print()
    res = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[i])):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        res.append(row)
    return f"the addition of both matrices is {res}"


# ########### Question_2 ############

# ###### Function 2 #######


def checkRotation(x, y):  # O(N^2) or O(x*y) x:matrix_len , y:sub_len
    print("\nFor the first Matrix:")
    matrix_1 = inputMatrix(x, y)
    print("\nFor the second Matrix:")
    matrix_2 = inputMatrix(y, x)
    for i in range(x):
        for j in range(y):
            if matrix_1[i][j] != matrix_2[j][i]:
                return "The two matrices are not rotational"
    return "The two matrices are rotational"


# ########### Question_3 ############

# ###### Inputs #######

def inputDictItemsNumber():  # O(N) N being the number of wrong inputs by the user
    num = input("Enter the number of items: ")
    while not num.isdigit():
        print("Number of items must be numeric")
        num = input("Enter the number of items again: ")
    return int(num)


def inputDict(n):  # O(N^2) or O(n*m) n:dict key:value pairs number , m:the number of wrong inputs by the user
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

def invertDictionary(dct):  # O(N) N:dict "key:value" pairs number
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
def intInputMatrix():  # O(N) N being the number of wrong inputs by the user
    num = input("Enter the number of Employee(s): ")
    while not num.isdigit():
        print("The number of employee(s) must me numeric")
        num = input("Enter the number of Employee(s) again: ")
    return int(num)


def inputMatrixEmployee(n):  # O(N^2) or O(N*M) N:the number of employees inputted by the user
    ids = []                                  # M:the number of wrong inputs by the user
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
    return matrix


# ###### Function 4 #######

def convertMatrixToDictionary(matrix):  # O(N) N:the number of employees inputted by the user
    dct = {}
    for i in range(len(matrix)):
        dct[matrix[i][2]] = [matrix[i][0], matrix[i][1], matrix[i][3], matrix[i][4]]
    return f"\nEmployee(s):\n{dct}"


# ########### Question_5 ############

# ###### Inputs #######

def inputCheckPalindrome():  # O(N) N being the number of wrong inputs by the user
    s = input("Enter a word: ")
    while len(s) == 0 or len(s.split()) > 1:
        print("You must enter one Word")
    return s


# ###### Function 5 #######

def checkPalindrome(s):  # O(N)  N:len(s) / 2
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return True and checkPalindrome(s[1:-1])


# ########### Question_6 ############

# ###### Inputs #######

def inputList():  # O(N) N being the number of wrong inputs by the user
    while True:
        try:
            lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
            return lst
        except ValueError:
            print("The list must be numbers!")


def mergeSort(lst):  # O(NlogN) N : len(lst) | "for both mergeSort(lst) and merge(left_half, right_half)"
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

        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1

        elif left_half[left_index] > right_half[right_index]:
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


def intInputNumber():  # O(N) N being the number of wrong inputs by the user
    num = input("Enter a number to look for: ")
    while not num.isdigit():
        print("This is not a numeric number!")
        num = input("Enter a number to look for again: ")
    return int(num)


# ###### Function 6 #######

def SearchElement(lst, k):  # O(N) N:len(lst)
    for i in range(len(lst)):
        if k == lst[i]:
            return f"The number {k} was found at index {i}\n"
    return f"The number {k} was not found"


# ###### Function 6(2) #######

def binarySearchElement(sorted_lst, k):  # O(logN) N:len(sorted_lst)
    print(f"After sorting the list:\n{sorted_lst}")
    low = 0
    high = len(sorted_lst) - 1
    while low <= high:
        middle = (low + high) // 2
        if k == sorted_lst[middle]:
            return f"The number {k} was found at index {middle}\n"
        elif k < sorted_lst[middle]:
            high = middle - 1
        elif k > sorted_lst[middle]:
            low = middle + 1
    return f"The number {k} was not found"


# ########### Menu ############

def Menu():  # O(1), only print
    print("""
    1. Add Matrices
    2. Check Rotation
    3. Invert Dictionary
    4. Convert Matrix to Dictionary
    5. Check Palindrome
    6. Search for an Element & Merge Sort
    7. Exit
    """)


# ########### Choice ############

def inputChoice():  # O(N) N being the number of wrong inputs by the user
    choice = input("Enter you choice: ")
    while not choice.isdigit():
        print("Your choice must be numeric.")
        choice = input("Enter you choice again: ")
    return int(choice)


def main():  # since the slowest of the functions is O(N^2), the main should be O(N^2)
    userLogin()
    Menu()
    choice = inputChoice()
    print()

    while choice != 7:
        if choice == 1:
            print(addMatrices(lenInput(), sublistLenInput()))
        elif choice == 2:
            print(checkRotation(lenInput(), sublistLenInput()))
        elif choice == 3:
            print(invertDictionary(inputDict(inputDictItemsNumber())))
        elif choice == 4:
            print(convertMatrixToDictionary(inputMatrixEmployee(intInputMatrix())))
        elif choice == 5:
            print(checkPalindrome(inputCheckPalindrome()))
        elif choice == 6:
            lst = inputList()
            k = intInputNumber()
            print(SearchElement(lst, k))
            print(binarySearchElement(mergeSort(lst), k))
        else:
            print("Your choice is INVALID")

        Menu()
        choice = inputChoice()
        print()

    print("\nYou EXITED the program...")


main()
