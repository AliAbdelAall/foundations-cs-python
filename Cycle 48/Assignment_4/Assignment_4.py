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
            print("Linked-List is empty!")
        else:
            current = self.head
            print("ll: Head-> ", end="")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def removeNode(self, value: int):
        if self.size == 0:
            print("Linked-List is empty!")

        elif self.size == 1:
            if self.head.data == value:
                self.head = None
                self.size -= 1
                print("Removed Node with value:", value)
            else:
                print("Could not find Node with value:", value)

        else:
            current = self.head
            previous = self.head
            while current:
                if current.data == value:
                    previous.next = current.next
                    current.next = None
                    self.size -= 1
                    print("Removed Node with value:", value)
                else:
                    previous = current
                    current = current.next
            print("Could not find Node with value:", value)


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
                        ll.removeNode(inputInteger())
                    else:
                        print("this choice is INVALID!")

                    displayLinkedListMenu()
                    choice_ll = inputStrChoice()

            elif choice == 2:
                pass
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
                displayStudentMenu()
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

                    displayStudentMenu()
                    choice_g = inputStrChoice()

        displayMainMenu()
        choice = inputIntChoice()


main()
