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
            lst = list(map(int,input("enter a list of number separated my spaces: ").split()))
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


def countTagInput():
    tag = input("Enter a tag : ")

    return tag

def htmlInput():
    html_code = """
<html> 
<head> 
<title>My Website</title> 
</head> 
<body> 
<h1>Welcome to my website!</h1> 
<p>Here you'll find information about me and my hobbies.</p> 
<h2>Hobbies</h2> 
<ul> 
<li>Playing guitar</li> 
<li>Reading books</li> 
<li>Traveling</li> 
<li>Writing cool h1 tags</li> 
</ul> 
</body> 
</html> """
    return html_code


def countTag(html_code, tag):
    tag_reader = "<" + tag + ">"
    if len(html_code) < len(tag_reader):
        return 0

    elif html_code[:len(tag_reader)] == tag_reader:
        return 1 + countTag(html_code[len(tag_reader):], tag)
    else:
        return countTag(html_code[1:], tag)


def choiceInput():    #handling user input to input only pisitive intrgers
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
            print("the number you entered have", countDigit(intInput()), "digit(s)")
        elif choice == 2:
            print("the max number is", findMax(findMaxInput()))
        elif choice == 3:
            print("your tag count is", countTag(htmlInput(), countTagInput()))
        else:
            print("this is an INVALID choice !")

        choiceMenu()
        choice = choiceInput()

    print("==============> THANK YOU FOR USING MY PROGRAM !!! :) <==============")


main()
