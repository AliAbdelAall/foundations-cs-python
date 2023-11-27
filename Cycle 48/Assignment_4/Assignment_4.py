# ----------- choice_1 ----------- #

# ------- classes ------- #

class Node:
    def __init__(self, data):  # O(1)
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # O(1)
        self.head = None
        self.size = 0

    def addNode(self, value):  # O(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return value

    def displayNodes(self):  # O(N) N: number of nodes
        if self.size == 0:
            print("\nLinked-List is empty!")
        else:
            current = self.head
            print("ll: Head-> ", end="")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def removeAllValueNodes(self, value):  # O(N) N: number of nodes
        if self.size == 0:
            print("\nLinked-List is empty!")

        else:
            current = self.head
            previous = None
            count = 0  # count is for the print and to check if we removed a node

            while current:
                if current.data == value:  # if we found the node we proceed
                    if not previous:  # if it is the first node
                        self.head = self.head.next
                        current = None
                    else:
                        previous.next = current.next
                        current.next = None  # we detach the node from the ll
                        current = previous.next
                    self.size -= 1
                    count += 1
                else:
                    previous = current  # we continue looping
                    current = current.next

            if count:
                print(f"\nRemoved {count} Node(s) with value:", value)
            else:
                print("\nNode with value:", value, ", was not found.")

    def removeNode(self, value):  # O(N) N: number of nodes
        if self.size == 0:
            return

        current = self.head  # same as before but we stop when we find and remove the node
        previous = None

        while current:
            if current.data == value:
                if not previous:
                    self.head = self.head.next
                    current.next = None
                else:
                    previous.next = current.next
                    current.next = None
                self.size -= 1
                return value  # we return the removed value for later use
            else:
                previous = current
                current = current.next
        return  # if not found we return None

    def checkConnectedNodes(self):  # O(N) N: number of nodes
        if self.size == 0:
            return
        else:  # we check the ll and we return the values inside the nodes as a list
            connected = []
            current = self.head
            while current:
                connected.append(current.data)
                current = current.next
            return connected


ll = LinkedList()


# ------- INPUTS ------- #

def inputInteger():  # O(N) N: wrong inputs by the user
    num = input("Enter a number: ").strip()
    while True:
        try:
            num = int(num)
            return str(num)
        except ValueError:
            print("This is not a Number!")
            num = input("Enter a number again: ").strip()


# ----------- choice_2 ----------- #

def checkPalindrome():  # O(N) N: len(s)
    s = input("Enter a string: ").strip()
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        stack = []
        mid = len(s) // 2  # for more optimization we have added mid
        for i in range(mid, len(s)):  # we add mid -> end of s to the stack
            stack.append(s[i])
        for j in range(0, mid):  # we check until mid, no extra steps needed
            if s[j] == stack[-1]:
                stack.pop()
            else:
                return False
    return True


# ----------- choice_3 ----------- #

# ------- INPUTS ------- #

def inputGrade(grade):  # O(N) N wrong inputs
    # this function handles user input of the grade
    grade = input(f"Enter student's {grade} Grade(0-100):").strip()
    while not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
        if not grade.isdigit():
            print("This is not a NUMERICAL Grade!")
        else:
            print("Grade must be between 0 and 100.")
        grade = input(f"Enter student's {grade} Grade(0-100) again:").strip()
    return int(grade)


def inputAttitude():  # O(N) N wrong inputs
    # this function handles user input
    attitude = input("Good Attitude? y(YES)/n(NO): ").strip()
    while attitude.lower() != "y" and attitude.lower() != "n":
        print("INVALID answer!")
        attitude = input("Good Attitude? y(YES)/n(NO): ")
    return True if attitude == "y" else False


# ------- CLASS ------- #

class Student:
    def __init__(self):  # O(N) since we have inputGrade() inside
        self.name = input("Enter Student Name: ").strip()
        self.midterm_grade = inputGrade("Midterm")
        self.final_grade = inputGrade("Final")
        self.good_attitude = inputAttitude()
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, new_student):
        if not self.size:
            self.head = new_student
        else:
            current = self.head
            previous = None
            inserted = False  # check if we inserted the node

            while current and not inserted:
                if new_student.good_attitude and not current.good_attitude:
                    # we give 1st priority here
                    if not previous:
                        new_student.next = self.head
                        self.head = new_student
                    else:
                        previous.next = new_student
                        new_student.next = current
                    inserted = True

                elif new_student.good_attitude == current.good_attitude:
                    # for same 1st priority
                    if new_student.final_grade > current.final_grade:
                        # we give 2nd priority here
                        if not previous:
                            new_student.next = self.head
                            self.head = new_student
                        else:
                            previous.next = new_student
                            new_student.next = current
                        inserted = True
                    elif new_student.final_grade == current.final_grade:
                        # for same 2nd priority
                        if new_student.midterm_grade >= current.midterm_grade:
                            # we give 3rd priority here
                            if not previous:
                                new_student.next = self.head
                                self.head = new_student
                            else:
                                previous.next = new_student
                                new_student.next = current
                            inserted = True

                previous = current
                current = current.next

            if not inserted:  # if student have the least priority we add it to the end
                previous.next = new_student

        self.size += 1

        print(f"""
New student added:
Name: {new_student.name}
Midterm grade: {new_student.midterm_grade}/100
Final Grade: {new_student.final_grade}/100
Good attitude: {new_student.good_attitude}
""")

    def dequeue(self):
        if not self.size:
            print("There is no students to interview!")
        else:
            print(f"""
student ready for interview:
Name: {self.head.name}
Midterm grade: {self.head.midterm_grade}/100
Final Grade: {self.head.final_grade}/100
Good attitude: {self.head.good_attitude}
""")
            current = self.head
            self.head = self.head.next
            current.next = None
        self.size -= 1

    def displayQueue(self):  # O(N) N:number of nodes
        # added this function just for bug fixing, it can be removed
        if not self.size:
            print("Queue is empty!")
        else:
            current = self.head
            print("Head: ", end="")
            while current is not None:
                print(current.name, end=" -> ")
                current = current.next
            print("None")


queue = PriorityQueue()


# ----------- choice_4 ----------- #

# ------- INPUTS ------- #
def validateInfix(expression):  # O(N) N: len(expression)
    valid_chars = set("0123456789*/+-() ")
    operators = set("*/+-")

    stack = []
    previous_char = None

    for char in expression:
        if char not in valid_chars:
            return False

        if previous_char and previous_char in operators and char in operators:
            return False

        if char == "(":
            stack.append(char)

        elif char == ")":
            if not stack:
                return False
            stack.pop()

        previous_char = char

    return len(stack) == 0


# ------- FUNCTION ------- #

def inputInfix():  # O(N) N: len(expression)
    # handles user input if the expression was in wrong format
    expression = input("Enter Infix expression: ").strip()
    valid = validateInfix(expression)
    while not valid:
        print("Invalid Infix Expression!")
        expression = input("Enter Infix expression again: ").strip()
        valid = validateInfix(expression)
    return expression


def evaluateInfix(expression):  # O(N) N: len(expression)
    operator_stack = []
    operand_stack = []

    operators = {'+', '-', '*', '/'}  # the set of operator makes a shortcut to check if it is an operator

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # priority as PEMDAS

    def applyOperation():  # O(1) we pop and compare
        # this nested function have access to all variables in the outer function
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        if operator == '+':
            operand_stack.append(operand1 + operand2)
        elif operator == '-':
            operand_stack.append(operand1 - operand2)
        elif operator == '*':
            operand_stack.append(operand1 * operand2)
        elif operator == '/':
            operand_stack.append(operand1 // operand2)

    for char in expression:  # we append each char to its corresponding stack
        if char == "":
            continue
        elif char.isdigit():
            operand_stack.append(int(char))
        elif char in operators:  # while appending we do the calculations
            while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence[char]:
                applyOperation()
            operator_stack.append(char)
        elif char == '(':  # we make sure we have valid parentheses
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                applyOperation()
            operator_stack.pop()

    while operator_stack:  # we do the calculations of the rest of the expression
        applyOperation()

    return operand_stack.pop()  # the last item on the stack will be the result


# ----------- choice_5 ----------- #

# ------- INPUTS ------- #
def inputVertex(_):  # O(N) N: wrong inputs by the user
    # we make sure the user inputs a number since vertices are numbers
    vertex = input(f"Enter {_} vertex: ").strip()
    while not vertex.isdigit():
        print("vertex must be numeric!")
        vertex = input(f"Enter {_} vertex again: ").strip()
    return vertex


# ------- CLASS ------- #
class Graph:
    def __init__(self):  # O(1)
        self.adj_list = {}
        self.vertex_num = "0"  # for auto-generating vertices

    def addVertex(self):  # O(1)
        self.adj_list[self.vertex_num] = LinkedList()
        print(f"Vertex {self.vertex_num} was added to the graph.")
        self.vertex_num = str(int(self.vertex_num) + 1)  # we increment and convert to string

    def checkVertices(self, v1, v2):  # O(1)
        # we check if the vertices exists
        if v1 in self.adj_list and v2 in self.adj_list:
            return [v1, v2]

        elif v1 not in self.adj_list and v2 not in self.adj_list:
            print(f"Both vertices {v1} and {v2} does not exist!\n")
        # extra steps to be user-friendly
        elif v1 not in self.adj_list:
            print(f"Vertex {v1} does not exist!\n")

        elif v2 not in self.adj_list:
            print(f"Vertex {v2} does not exist!\n")

    def addEdge(self, v1, v2):  # O(N) since we have checkConnectedNodes() inside
        checked = self.checkVertices(v1, v2)
        if checked:
            connected = self.adj_list[v1].checkConnectedNodes()  # O(N)
            if not connected or v2 not in connected:
                self.adj_list[v1].addNode(v2)
                self.adj_list[v2].addNode(v1)
                print(f"Added and Edge between vertex {v1} and vertex {v2}.")
            else:
                print(f"Edge between vertex {v1} and vertex {v2} already exist.")

    def removeVertex(self, vertex):  # O(N^2) N: number of edges
        if vertex not in self.adj_list:
            print(f"Vertex {vertex} does not exist")

        else:
            # to remove a vertex we need to remove all its edges too
            connected = self.adj_list[vertex].checkConnectedNodes()  # O(N)
            if connected:
                for v in connected:  # O(N)
                    self.adj_list[v].removeNode(vertex)  # O(N)

            del self.adj_list[vertex]
            print(f"Removed Vertex {vertex} from graph")

    def removeEdge(self, v1, v2):  # O(N) N: number of nodes
        if not self.adj_list:
            print("Graph is empty! Add vertices and edges first.")
            return
        checked = self.checkVertices(v1, v2)
        if checked:
            removed = self.adj_list[v1].removeNode(v2)  # O(N)
            if removed:
                self.adj_list[v2].removeNode(v1)  # O(N)
                print(f"Removed Edge between vertex {v1} and vertex {v2}.")
            else:
                print(f"Edge between vertex {v1} and vertex {v2} does not exist!")

    def displayGraph(self, vertex):  # O(V)
        if not self.adj_list:
            print("Graph is empty add a vertex first!")
        else:
            if vertex not in self.adj_list:
                print("vertex does not exist")
            else:
                s = ""
                for v in self.adj_list:
                    if v >= vertex:  # we can compare numbers even as string (ASCII)
                        s += v + ","
                if s:
                    print(s.strip(","))
                else:
                    print("No vertices found at degree", vertex, "or above")

    def displayConnectedVertices(self):  # O(N) since we have displayNodes() inside
        # this is just for testing and bug fixing, it can be removed
        vertex = inputVertex("")
        if vertex not in self.adj_list:
            print("vertex does not exist")
        else:
            self.adj_list[vertex].displayNodes()  # O(N)


graph = Graph()


# ----------- MENUS ----------- #

def displayMainMenu():  # O(1)
    print("""
1. Singly Linked List
2. Check if Palindrome
3. Priority Queue
4. Evaluate an Infix Expression
5. Graph
6. Exit
""")


def displayLinkedListMenu():  # O(1)
    print("""
    a. Add Node
    b. Display Nodes
    c. Search for & Delete Node
    d. Return to main menu
    """)


def displayStudentMenu():  # O(1)
    print("""
    a. Add a student
    b. Interview a student
    c. Return to main menu
    """)


def displayGraphMenu():  # O(1)
    print("""
    a. Add vertex
    b. Add edge
    c. Remove vertex
    d. Remove edge
    e. Display vertices with a degree of X or more.
    f. Return to main menu
    """)


# ----------- CHOICE ----------- #

def inputIntChoice():  # O(N) N: wrong inputs by the user
    attempts = 3
    choice = input("Enter a number as your choice: ").strip()
    while not choice.isdigit() or int(choice) < 1 or int(choice) > 7:
        if attempts == 0:
            return
        print("INVALID! Your Choice MUST be a POSITIVE numerical number 0->6")
        print(f"you still have {attempts} attempts\n")
        choice = input("Enter a number as your choice again: ").strip()
        attempts -= 1
    return int(choice)


def inputStrChoice():  # O(N) N: wrong inputs by the user
    choice = input("Enter a letter as your choice: ").strip()
    while len(choice) != 1 or choice.isdigit():
        print("your choice must be one letter!\n")
        choice = input("Enter a letter as your choice again: ").strip()
    return choice


# ----------- User Greeting ----------- #

def greetUser():  # O(1)
    name = input("Enter your name: ").strip()
    if name == "":
        name = "Anonymous"
    print(f"Welcome, {name}!")


# ----------- MAIN ----------- #

def main():  # O(N^2) since we have graph.removeVertex()  # O(N^2) inside
    greetUser()  # O(1)
    displayMainMenu()  # O(1)
    choice = inputIntChoice()  # O(N)
    if not choice:
        print("you have reach MAX-LIMIT of ATTEMPTS!\n\n Exiting the program....")
        return

    while choice != 6:

        if choice == 1:
            displayLinkedListMenu()  # O(1)
            choice_ll = inputStrChoice()  # O(N)

            while choice_ll != "d":
                if choice_ll == "a":
                    value = inputInteger()  # O(N)
                    ll.addNode(value)
                    print(f"New Node with value: {value}, added.")
                elif choice_ll == "b":
                    ll.displayNodes()  # O(N)
                elif choice_ll == "c":
                    ll.removeAllValueNodes(inputInteger())  # O(N)
                else:
                    print("this choice is INVALID!")

                displayLinkedListMenu()  # O(1)
                choice_ll = inputStrChoice()  # O(N)

        elif choice == 2:
            print(checkPalindrome())  # O(N)
        elif choice == 3:
            displayStudentMenu()  # O(1)
            choice_s = inputStrChoice()  # O(N)

            while choice_s != "c":
                if choice_s == "a":
                    queue.enqueue(Student())  # O(N)
                elif choice_s == "b":
                    queue.dequeue()  # O(1)
                # elif choice_s == "d":
                #     queue.displayQueue()
                else:
                    print("this choice is INVALID!")

                displayStudentMenu()
                choice_s = inputStrChoice()

        elif choice == 4:
            print(evaluateInfix(inputInfix()))
        elif choice == 5:
            displayGraphMenu()  # O(1)
            choice_g = inputStrChoice()  # O(N)

            while choice_g != "f":
                if choice_g == "a":
                    graph.addVertex()  # O(1)
                elif choice_g == "b":
                    graph.addEdge(inputVertex("first"), inputVertex("second"))  # O(N)
                elif choice_g == "c":
                    graph.removeVertex(inputVertex(""))  # O(N^2)
                elif choice_g == "d":
                    graph.removeEdge(inputVertex("first"), inputVertex("second"))  # O(N)
                elif choice_g == "e":
                    graph.displayGraph(inputVertex(""))  # O(N)
                # elif choice_g == "g":
                #     graph.displayConnectedVertices()  # o(N)
                else:
                    print("this choice is INVALID!")

                displayGraphMenu()  # O(1)
                choice_g = inputStrChoice()  # O(N)

        displayMainMenu()  # O(1)
        choice = inputIntChoice()  # O(N)

    print("Exiting the program ...")


main()
