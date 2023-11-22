# ----------- choice_1 ----------- #

# ------- classes ------- #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, value: int):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f"New Node with value: {value}, added.")

    def displayNodes(self):
        if self.size == 0:
            print("\nLinked-List is empty!")
        else:
            current = self.head
            print("ll: Head-> ", end="")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def removeNodes(self):
        if self.size == 0:
            print("\nLinked-List is empty!")

        else:
            value = inputInteger()
            current = self.head
            previous = None
            count = 0

            while current:
                if current.data == value:
                    if previous:
                        previous.next = current.next
                        current.next = None
                        current = previous.next
                    else:
                        self.head = current.next
                        current = current.next
                    self.size -= 1
                    count += 1
                else:
                    previous = current
                    current = current.next

            if count:
                print(f"\nRemoved {count} Node(s) with value:", value)
            else:
                print("\nNode with value:", value, ", was not found.")


ll = LinkedList()


# ------- INPUTS ------- #

def inputInteger():
    num = input("Enter a number: ").strip()
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            print("This is not a Number!")
            num = input("Enter a number again: ").strip()


# ----------- choice_2 ----------- #

def checkPalindrome():
    s = input("Enter a string: ")
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
        for j in range(len(s)):
            if s[j] == stack[-1]:
                stack.pop()
            else:
                return False
    return True


# ----------- choice_3 ----------- #

# ------- INPUTS ------- #

def inputGrade():
    grade = input("Enter student's NUMERICAL Grade(0-100):")
    while not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
        if not grade.isdigit():
            print("This is not a NUMERICAL Grade!")
        else:
            print("Grade must be between 0 and 100.")
        grade = input("Enter student's NUMERICAL Grade(0-100) again:")


class Student:
    def __init__(self, name, midterm_grade: int, final_grade: int, good_attitude: bool):
        self.name = input("Enter Student Name: ")
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude


# ----------- MENUS ----------- #

def displayMainMenu():
    print("""
1. Singly Linked List
2. Check if Palindrome
3. Priority Queue
4. Evaluate an Infix Expression
5. Graph
6. Exit
""")


def displayLinkedListMenu():
    print("""
    a. Add Node
    b. Display Nodes
    c. Search for & Delete Node
    d. Return to main menu
    """)


def displayStudentMenu():
    print("""
    a. Add a student
    b. Interview a student
    c. Return to main menu
    """)


def displayGraphMenu():
    print("""
    a. Add vertex
    b. Add edge
    c. Remove vertex
    d. Remove edge
    e. Display vertices with a degree of X or more.
    f. Return to main menu
    """)


# ----------- CHOICE ----------- #

def inputIntChoice():
    choice = input("Enter a number as your choice: ").strip()
    while not choice.isdigit():
        print("this is not a number!")
        choice = input("Enter a number as your choice again: ").strip()
    return int(choice)


def inputStrChoice():
    choice = input("Enter a letter as your choice: ").strip()
    while len(choice) != 1:
        print("your choice must be one letter!")
        choice = input("Enter a letter as your choice again: ").strip()
    return choice


# ----------- User Greeting ----------- #

def greetUser():
    name = input("Enter your name: ").strip()
    if name == "":
        name = "Anonymous"
    print(f"Welcome, {name}!")


# ----------- MAIN ----------- #

def main():
    greetUser()
    displayMainMenu()
    choice = inputIntChoice()
    error_count = 0

    while choice != 6 and error_count != 4:
        if choice > 6 or choice < 1:
            print("this choice is INVALID!")
            print(f"you still have {4 - error_count} attempts")
            error_count += 1

        else:
            error_count = 0
            if choice == 1:
                displayLinkedListMenu()
                choice_ll = inputStrChoice()

                while choice_ll != "d":
                    if choice_ll == "a":
                        ll.addNode(inputInteger())
                    elif choice_ll == "b":
                        ll.displayNodes()
                    elif choice_ll == "c":
                        ll.removeNodes()
                    else:
                        print("this choice is INVALID!")

                    displayLinkedListMenu()
                    choice_ll = inputStrChoice()

            elif choice == 2:
                print(checkPalindrome())
            elif choice == 3:
                displayStudentMenu()
                choice_s = inputStrChoice()

                while choice_s != "c":
                    if choice == "a":
                        pass
                    elif choice == "b":
                        pass
                    else:
                        print("this choice is INVALID!")

                    displayStudentMenu()
                    choice_s = inputStrChoice()

            elif choice == 4:
                pass
            elif choice == 5:
                displayGraphMenu()
                choice_g = inputStrChoice()

                while choice_g != "f":
                    if choice == "a":
                        pass
                    elif choice == "b":
                        pass
                    elif choice == "c":
                        pass
                    elif choice == "d":
                        pass
                    elif choice == "e":
                        pass
                    else:
                        print("this choice is INVALID!")

                    displayGraphMenu()
                    choice_g = inputStrChoice()

        displayMainMenu()
        choice = inputIntChoice()


main()
