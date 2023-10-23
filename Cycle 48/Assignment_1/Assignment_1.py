########  Question_1  ########

"""
a. 915
b. 897
c. 897
d. 915.0
e. 1
f. 2.5
g. 2.5
h. 2.5
i. 2.5
g. 0
"""
expression = [
    10 * (90 + 2) - 5,
    10 * 90 + 2 - 5,
    10 * 90 + (2 - 5),
    10.0 * (90 + 2) - 5,
    120 / (20 + 40) - (6 - 2) / 4,
    5.0 / 2,
    5 / 2,
    5.0 / 2.0,
    5 / 2.0,
    678 % 3 * (8 - (9 / 4))]


def calcExp(arr):
    for item in arr:
        print(item)


# calcExp(expression)

########  Question_2  ########

def inputID():
    id = input("Enter your ID number: ").strip()
    while not id.isdigit():
        print("this is not a number")
        id = input("Enter your ID number again: ").strip()
    return "0" + id


def inputName():
    name = input("Enter your name: ").strip()
    return name.upper()


def inputDOB():
    b_date = input("Enter your Date of Birth (DD/MM/YYYY): ").strip()
    b_date.replace("-", "/")
    return b_date


def inputAdress():
    adress = input("Enter your Adress: ").strip()
    return adress.lower()


def readInput():
    id = inputID()
    name = inputName()
    b_date = inputDOB()
    adress = inputAdress()
    print(f"Your profile - ID: [{id}], name: [{name}], DOB: [{b_date}], Address: [{adress}]")


# #######  Question_3  ########

def countDigits():
    num = input("Enter a number: ").strip()
    count = 0
    while not num.isdigit():
        print("this is not a number")
        num = input("Enter a number again: ").strip()
    # print(f"this number contains {len(num)} digits")

    for i in range(len(num)):
        count += 1
    print(f"this number contains {count} digits")


########  Question_4  ########

def gradeInput():
    grade = input("Enter your numeric grade: ")
    while not grade.isdigit() and int(grade) <= 100:
        print("your grade must be numeric and between(0-100).")
        grade = input("Enter your numeric grade again: ").strip()
    return int(grade)


def letterGrade(gr):
    if gr >= 97:
        print(f"{gr} is equivalent to a A+.")

    elif gr >= 93 and gr < 97:
        print(f"{gr} is equivalent to a A.")

    elif gr >= 90 and gr < 93:
        print(f"{gr} is equivalent to a A-.")

    elif gr >= 87 and gr < 90:
        print(f"{gr} is equivalent to a B+.")

    elif gr >= 83 and gr < 87:
        print(f"{gr} is equivalent to a B.")

    elif gr >= 80 and gr < 83:
        print(f"{gr} is equivalent to a B-.")

    elif gr >= 77 and gr < 80:
        print(f"{gr} is equivalent to a C+.")

    elif gr >= 73 and gr < 77:
        print(f"{gr} is equivalent to a C.")

    elif gr >= 70 and gr < 73:
        print(f"{gr} is equivalent to a C-.")

    elif gr >= 67 and gr < 70:
        print(f"{gr} is equivalent to a D+.")

    elif gr >= 63 and gr < 67:
        print(f"{gr} is equivalent to a D.")

    elif gr >= 60 and gr < 63:
        print(f"{gr} is equivalent to a D-.")

    else:
        print(f"{gr} is equivalent to a F.")


########  Question_5  ########

def numInput():
    num = input("Enter a number: ")
    while not num.isdigit():
        print("this is not a number")
        num = input("Enter a number again: ")
    return int(num)


def printStarts(n):
    j = 1
    for i in range((n * 2) - 1):
        print("*" * j)
        if j < n and i < n:
            j += 1
        else:
            j -= 1


########  Question_6  ########

def printEvenNums(n, m):
    print(f"\nThe even numbers between {n} and {m} are:")
    for i in range(n, m + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()


########  Display_Menu  ########

def DisplayMenu():
    print("""
  1- Calculate Expressions
  2- Read Profile
  3- Count Digits
  4- Letter Grade
  5- Print Stars
  6- Print Even Numbers
  """)


########  Choice Input  ########

def inputChoice():
    choice = input("Enter your choice: ")
    while not choice.isdigit():
        print("this is not a number")
        choice = input("Enter your choice again: ")
    return int(choice)


##########  Main  ##########

def main():
    DisplayMenu()

    choice = inputChoice()
    while choice != 0:
        if choice == 1:
            calcExp(expression)
        elif choice == 2:
            readInput()
        elif choice == 3:
            countDigits()
        elif choice == 4:
            letterGrade(gradeInput())
        elif choice == 5:
            printStarts(numInput())
        elif choice == 6:
            printEvenNums(numInput(), numInput())
        else:
            print("this choice is UNAVAILABLE.")

        DisplayMenu()
        choice = inputChoice()


main()
