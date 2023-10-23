# ################## Question_1 ###################

# ########## Inputs ###########

def intInput():
    num = input("Enter a number: ")
    while not num.isdigit():
        print("This is not a number!")
        num = input("Enter a number again: ")
    return int(num)


def strInput():
    s = input("Enter a string: ")
    return s


# ########## function_1 ###########

def ReversedMultipliedString(s, i):
    # s1 = ""
    # for i in range(len(s) - 1, -1, -1):
    #     s1 += s[i]
    # return s1 * i

    # return s.reverse() * i

    return s[::-1] * i


# ################## Question_2 ###################

# ########## function_2 ###########

def arrangeLetters(s):
    s_upper = ""
    s_lower = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s_upper += s[i]
            elif s[i].islower():
                s_lower += s[i]
    return s_upper + s_lower


# ################## Question_3 ###################

# ########## Inputs ###########

# ###### Method_1 ########

# def str1Input():
#     s = input("Enter the 1st string: ")
#     return sorted(s)
#
# def str2Input():
#     s = input("Enter the 2nd string: ")
#     return sorted(s)

# ###### Method_2 ########

def str1Input():
    s = input("Enter the 1st string: ")
    return s


def str2Input():
    s = input("Enter the 2nd string: ")
    return s


# ########## function_3 ###########

# every method have its input function and the function itself
# if you want to test it make sure comment/uncomment the right functions

# ###### Method_1 ########

# def validAnagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             return False
#     return True

# ###### Method_2 ########
def validAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count_s1, count_s2 = {}, {}

    # ###### Method_2(1) ########
    for i in range(len(s1)):
        count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
        count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)

    # ###### Method_2(2) ########
    # here we did not use the ".get()" method

    # for i in range(len(s1)):
    #     if s1[i] in count_s1:
    #         count_s1[s1[i]] += 1
    #     else:
    #         count_s1[s1[i]] = 1
    #
    #     if s2[i] in count_s2:
    #         count_s2[s2[i]] += 1
    #     else:
    #         count_s2[s2[i]] = 1

    for key in count_s1:
        if count_s1[key] != count_s2.get(key, 0):
            return False

    return True


# ################## Question_4 ###################

# ########## Inputs ###########

def listInput():
    while True:
        try:
            lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
            return lst
        except ValueError():
            print("The list must be numbers!")


# ########## menu ###########

def miniMenu():
    print("""
    1- Find highest number
    2- Find Lowest number
    0- Back
    """)


# ########## function_4(1) ###########

def highestValue(lst):
    h = lst[0]
    for i in range(len(lst)):
        if lst[i] > h:
            h = lst[i]
    print(f"the highest value in the list is {h} at index {lst.index(h)}")


# ########## function_4(2) ###########

def lowestValue(lst):
    h = lst[0]
    for i in range(len(lst)):
        if lst[i] < h:
            h = lst[i]
    print(f"the lowest value in the list is {h} at index {lst.index(h)}")


# ################## Question_5 ###################

def sumDigit(num):
    if num < 10:
        return num
    return num % 10 + sumDigit(num // 10)


# ################## Question_6 ###################

def removeConsDup(s, i=0):
    if i == len(s) - 1:
        return s
    if s[i] == s[i + 1]:
        s = s[:i] + s[i + 1:]
    else:
        i += 1
    return removeConsDup(s, i)


# ###### **EXTRA** ########

# ################## Question_7 ###################

# # if you want to test it make sure comment the other function

# ###### Method_1 ########

# def reverseDigits(num, m=1):
#     if num < 10:
#         return num
#     while num % m != num:
#         m *= 10
#     m //= 10
#     return (num % 10 * m) + reverseDigits(num // 10, m // 10)

# ###### Method_2 ########
def reverseDigits(num, reversed_n=0):
    if num == 0:
        return reversed_n
    last_digit = num % 10
    reversed_n = reversed_n * 10 + last_digit
    return reverseDigits(num // 10, reversed_n)


# ################## Display Menu ###################

def displayMenu():
    print("""The choice Menu:
    1- Reverse and Multiply
    2- Rearrange Letters
    3- Valid Anagram
    4- Max or Min 
    5- Digit Sum
    6- Remove Duplicates
    7- Reverse Number Digits
    0- Exit
    """)


# ################## Choice Input ###################

def choiceInput():
    choice = input("Enter your choice: ")
    while not choice.isdigit():
        print("This is not a number!")
        choice = input("Enter your choice again: ")
    return int(choice)


# ################## Main ###################

def main():
    displayMenu()
    choice = choiceInput()

    while choice != 0:
        if choice == 1:
            print(ReversedMultipliedString(strInput(), intInput()))

        elif choice == 2:
            print(arrangeLetters(strInput()))

        elif choice == 3:
            print(validAnagram(str1Input(), str2Input()))

        elif choice == 4:
            miniMenu()
            choice1 = choiceInput()
            while choice1 != 0:
                if choice1 == 1:
                    highestValue(listInput())

                elif choice1 == 2:
                    lowestValue(listInput())

                else:
                    print("This choice is INVALID")
                miniMenu()
                choice1 = choiceInput()
        elif choice == 5:
            print(sumDigit(intInput()))

        elif choice == 6:
            print(removeConsDup(strInput(), i=0))
        elif choice == 7:
            print(reverseDigits(intInput(), reversed_n=0))

        else:
            print("this choice is INVALID.")

        displayMenu()
        choice = choiceInput()

    print("you Exited the program...")


main()
