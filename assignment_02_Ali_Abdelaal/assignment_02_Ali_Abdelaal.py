

def intInput(): #handling user input to input only pisitive intrgers
    while True:
        try:
            n = input("enter a number : ")
            num = int(n)
            if num < 0:
                print("This is a negative number")
            else:
                return num
        except ValueError:
            print("this is not a number.")


def countDigit(num):
    if num < 10 and num >=0: #if we devide the number by 10 then we remove a digit  and we count how many times we divides the number by using recursion and the last didgit will be counted also
        return 1
    else:
        return 1 + countDigit(num/10)




def findMaxInput(): #handling user input to enter only a list of in seperated by spaces
    while True:
        try:
            lst = list(map(int,input("enter a number a list of number separated my spaces: ").split()))
            return lst
        except ValueError:
            print("the list must be numbers.")


def findMax(lst):
    if len(lst) == 1: #if there is one element in the list this is the sign of the end of recursion
        return lst[0]

    else:
        if lst[0] > findMax(lst[1:]): #this recursion will check the for the max element for last index (len(lst)-1) to the first index [0] caomparing 2 elements at a time
            return lst[0]
        else:
            return findMax(lst[1:])


# def countTagsInput():
#     print("Enter your HTML code : ")
#     lists = []
#     tag_separators = ["<", ">"]
#     while True:
#         s = input()
#         if s:
#             for separator in tag_separators:
#                 s = s.replace(separator, "|")
#             result = s.split("|")
#             lists.append(result)
#         else:
#             break
#     return lists
#
#
# def countTags(lst):
#     tag = input("Enter a tag : ")
#     counter = 0
#     for line in lst:
#         if line[1] == tag and line[-1] == "/"+tag:
#             counter += 1
#     result = "this tag "+tag+" have been repeated "+str(counter)+ "times."
#     return result
#
#
# print(countTags(countTagsInput()))
########### This code is yet to be finished #############

def choiceInput(): #handling user input to input only pisitive intrgers
    while True:
        try:
            n = input("What is your choice ? : ")
            num = int(n)
            if num < 0:
                print("This is a negative number")
            else:
                return num
        except ValueError:
            print("this is not a number.")

def choiceMenu():
    print("1. Count Digits\n" + "2. Find Max\n" + "3. Count Tags\n" + "4. Exit ")
def main():
    choiceMenu()
    choice = choiceInput()
    while choice != 4:
        if choice == 1:
            print(countDigit(intInput()))
        elif choice == 2:
            print(findMax(findMaxInput()))
        elif choice == 3:
            print("-----this part of the program is still under development :)-----")
        else:
            print("this is an INVALID number !")

        choiceMenu()
        choice = choiceInput()

    print("==> my assignment is not finished perfectly yet but i am still working on it :) <==")


main()
